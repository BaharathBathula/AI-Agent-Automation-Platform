from sqlalchemy.orm import Session
from datetime import datetime
from app.db.models.run import Run


class RunService:

    @staticmethod
    def create_run(db: Session, task_id: int):
        run = Run(
            task_id=task_id,
            status="running",
            started_at=datetime.utcnow()
        )

        db.add(run)
        db.commit()
        db.refresh(run)

        return run

    @staticmethod
    def complete_run(db: Session, run: Run, output: str):
        run.status = "completed"
        run.output = output
        run.completed_at = datetime.utcnow()

        db.commit()
        return run

    @staticmethod
    def fail_run(db: Session, run: Run, error: str):
        run.status = "failed"
        run.error = error
        run.completed_at = datetime.utcnow()

        db.commit()
        return run
