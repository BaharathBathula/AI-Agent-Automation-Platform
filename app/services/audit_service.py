from sqlalchemy.orm import Session
from app.db.models.audit_log import AuditLog


class AuditService:

    @staticmethod
    def log(db: Session, run_id: int, event_type: str, message: str):
        log = AuditLog(
            run_id=run_id,
            event_type=event_type,
            message=message
        )

        db.add(log)
        db.commit()

        return log
