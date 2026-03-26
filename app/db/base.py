from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import models here so SQLAlchemy detects them
from app.db.models.task import Task
from app.db.models.run import Run
from app.db.models.audit_log import AuditLog
