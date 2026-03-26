from celery.schedules import crontab
from app.workers.celery_app import celery_app


celery_app.conf.beat_schedule = {
    "run-daily-agent-task": {
        "task": "execute_agent_task",
        "schedule": crontab(minute=0, hour=9),
        "args": (1, "Daily automation task")
    }
}
