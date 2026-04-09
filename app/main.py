import os
from contextlib import asynccontextmanager

from starlette.templating import Jinja2Templates
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.responses import Response
from sqlalchemy.orm import Session
from openai import OpenAI
from dotenv import load_dotenv

from .database import engine, SessionLocal, get_db, Base
from .models import Task

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="AI Task Tagger", lifespan=lifespan)

templates = Jinja2Templates(directory="templates")


def render_template(name: str, context: dict) -> Response:
    """Render template manually to avoid Starlette 1.0 caching bug."""
    template = templates.get_template(name)
    html = template.render(**context)
    return HTMLResponse(content=html)


def get_ai_tag(task_text: str) -> str:
    """Request a single-word tag from OpenRouter AI."""
    try:
        response = client.chat.completions.create(
            model="liquid/lfm-2.5-1.2b-instruct:free",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional task classifier. Your goal is to provide a 1-2 word category in English.\n"
                        "Rules:\n"
                        "1. Analyze the intent of the task.\n"
                        "2. Use diverse categories: 'Education', 'Work', 'Fitness', 'Groceries', 'Habits', 'Finance', 'Home', 'Entertainment'.\n"
                        "3. If the task doesn't fit, create a new accurate category (1-2 words).\n"
                        "Examples:\n"
                        "'solve equations' -> Education\n"
                        "'buy milk' -> Groceries\n"
                        "'run 5km' -> Fitness\n"
                        "'smoke' -> Habits\n"
                        "'fix code' -> Development\n"
                        "Output ONLY the word. No explanations, no dots."
                    ),
                },
                {"role": "user", "content": task_text},
            ],
            max_tokens=10,
            temperature=0.3,
        )
        tag = (
            response.choices[0]
            .message.content.strip()
            .split()[0]
            .lower()
            .replace(".", "")
        )
        return tag if tag else "uncategorized"
    except Exception as e:
        print(f"AI tagging error: {e}")
        return "uncategorized"


@app.get("/", response_class=HTMLResponse)
async def index(request: Request, db: Session = Depends(get_db)):
    tasks = db.query(Task).order_by(Task.id.desc()).all()
    return render_template("index.html", {"request": request, "tasks": tasks})


@app.post("/tasks")
async def create_task(
    username: str = Form(...),
    task_text: str = Form(...),
    db: Session = Depends(get_db),
):
    ai_tag = get_ai_tag(task_text)
    task = Task(username=username, task_text=task_text, ai_tag=ai_tag)
    db.add(task)
    db.commit()
    db.refresh(task)
    return RedirectResponse(url="/", status_code=303)


@app.post("/tasks/{task_id}/delete")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return RedirectResponse(url="/", status_code=303)
