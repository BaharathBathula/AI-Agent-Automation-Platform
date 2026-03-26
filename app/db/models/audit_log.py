from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.db.base import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer, nullable=False)

    event_type = Column(String)
    message = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
