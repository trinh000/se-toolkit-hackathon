# AI Task Tagger

A web task manager that automatically tags your tasks using AI (OpenRouter / Gemini 2.5 Flash).

## Demo

![Demo](https://via.placeholder.com/800x400?text=AI+Task+Tagger+Demo)

## Product Context

AI Task Tagger was built for the hackathon to demonstrate how lightweight LLM APIs can add smart metadata to everyday workflows. Instead of manually categorizing tasks, a single AI call assigns a descriptive tag — instantly.

## Features

- **Auto-tagging** — Every task is sent to OpenRouter (Gemini 2.5 Flash) which returns a single descriptive tag
- **Persistent storage** — Tasks are saved in a SQLite database
- **Clean UI** — Responsive TailwindCSS interface with gradient accents
- **Delete tasks** — Hover over any task to remove it
- **Docker-ready** — One-command deployment via docker-compose

## Tech Stack

| Layer       | Technology              |
|-------------|-------------------------|
| Backend     | FastAPI + Python 3.11   |
| Database    | SQLite + SQLAlchemy     |
| Frontend    | Jinja2 + TailwindCSS    |
| AI          | OpenRouter (Gemini 2.5 Flash) |
| Deployment  | Docker + docker-compose |

## Usage

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd se-toolkit-hackathon
   ```

2. **Set your API key**
   ```bash
   # Edit .env and add your OpenRouter key
   OPENROUTER_API_KEY=sk-or-your-actual-key-here
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

5. **Open** http://localhost:8000

### Add a Task

1. Enter your name and task description
2. Click "Add Task & Auto-Tag"
3. Watch the AI assign a tag in real-time

## Deployment

### Docker Compose (Recommended)

```bash
# Make sure your .env has a valid OPENROUTER_API_KEY
docker compose up --build
```

The app will be available at http://localhost:8000

### Docker (manual)

```bash
docker build -t ai-task-tagger .
docker run -p 8000:8000 --env-file .env ai-task-tagger
```

### Production Notes

- Replace SQLite with PostgreSQL for production (change `DATABASE_URL`)
- Set a proper secret key and use HTTPS
- Consider caching AI responses for repeated task patterns

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app & AI tagging logic
│   ├── models.py        # SQLAlchemy Task model
│   └── database.py      # Database engine & session
├── templates/
│   └── index.html       # Jinja2 + TailwindCSS UI
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image
├── docker-compose.yml   # Docker orchestration
├── LICENSE              # MIT License
└── README.md            # This file
```

## License

MIT — see [LICENSE](LICENSE) for details.
