from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.db.models.run import Run

router = APIRouter()


@router.get("/runs/{run_id}")
def get_run(run_id: int, db: Session = Depends(get_db)):
    run = db.query(Run).filter(Run.id == run_id).first()

    if not run:
        return {"error": "Run not found"}

    return {
        "id": run.id,
        "task_id": run.task_id,
        "status": run.status,
        "output": run.output,
        "error": run.error
    }
