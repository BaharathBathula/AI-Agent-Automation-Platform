from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.db.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    prompt = Column(Text, nullable=False)
    agent_type = Column(String, default="planner_executor")
    priority = Column(String, default="medium")
    status = Column(String, default="pending")

    created_at = Column(DateTime, default=datetime.utcnow)
