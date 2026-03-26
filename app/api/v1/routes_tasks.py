from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

router = APIRouter()


class TaskCreateRequest(BaseModel):
    title: str = Field(..., example="Summarize support tickets")
    prompt: str = Field(..., example="Read support tickets and summarize the top 5 issues")
    agent_type: str = Field(default="planner_executor")
    priority: str = Field(default="medium")
    metadata: Optional[Dict[str, Any]] = None


@router.post("/tasks")
def create_task(payload: TaskCreateRequest):
    return {
        "message": "Task accepted",
        "task": payload.model_dump()
    }
