from sqlalchemy import Column, Integer, String, Text
from .database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    task_text = Column(Text, nullable=False)
    ai_tag = Column(String(50), nullable=True)
