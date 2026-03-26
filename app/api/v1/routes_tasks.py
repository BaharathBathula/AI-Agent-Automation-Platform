from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, Dict, Any

from app.api.deps import get_db
from app.services.task_service import TaskService
from app.services.run_service import RunService
from app.services.audit_service import AuditService
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

    # 1. Create task
    task = TaskService.create_task(db, payload)

    # 2. Create run
    run = RunService.create_run(db, task.id)

    try:
        runner = AgentRunner()

        # 3. Execute agent
        result = runner.run(payload.prompt, run_id=run.id, db=db)

        # 4. Complete run
        RunService.complete_run(db, run, str(result))

        return {
            "task_id": task.id,
            "run_id": run.id,
            "status": "completed",
            "execution": result
        }

    except Exception as e:

        RunService.fail_run(db, run, str(e))

        return {
            "task_id": task.id,
            "run_id": run.id,
            "status": "failed",
            "error": str(e)
        }
