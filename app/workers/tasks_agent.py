from app.workers.celery_app import celery_app
from app.db.session import SessionLocal
from app.services.run_service import RunService
from app.services.audit_service import AuditService
from app.orchestration.agent_runner import AgentRunner


@celery_app.task(name="execute_agent_task")
def execute_agent_task(task_id: int, prompt: str):

    db = SessionLocal()

    # Create run
    run = RunService.create_run(db, task_id)

    try:
        runner = AgentRunner()

        # Execute agent
        result = runner.run(prompt, run_id=run.id, db=db)

        # Complete run
        RunService.complete_run(db, run, str(result))

        return {"status": "completed", "run_id": run.id}

    except Exception as e:

        RunService.fail_run(db, run, str(e))

        return {"status": "failed", "error": str(e)}

    finally:
        db.close()
