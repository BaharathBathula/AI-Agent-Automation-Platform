from sqlalchemy.orm import Session
from app.db.models.task import Task


class TaskService:

    @staticmethod
    def create_task(db: Session, data):
        task = Task(
            title=data.title,
            prompt=data.prompt,
            agent_type=data.agent_type,
            priority=data.priority,
        )

        db.add(task)
        db.commit()
        db.refresh(task)

        return task
