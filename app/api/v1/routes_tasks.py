from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

from app.api.deps import get_db
from app.services.task_service import TaskService
from app.orchestration.agent_runner import AgentRunner

router = APIRouter()


class TaskCreateRequest(BaseModel):
    title: str
    prompt: str
    agent_type: str = "planner_executor"
    priority: str = "medium"
    metadata: Optional[Dict[str, Any]] = None


@router.post("/tasks")
def create_task(payload: TaskCreateRequest, db: Session = Depends(get_db)):

    # 1. Save task
    task = TaskService.create_task(db, payload)

    # 2. Run agent (sync for now)
    runner = AgentRunner()
    result = runner.run(payload.prompt)

    return {
        "task_id": task.id,
        "status": "completed",
        "execution": result
    }
