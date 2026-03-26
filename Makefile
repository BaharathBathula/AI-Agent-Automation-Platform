run:
	uvicorn app.main:app --reload

worker:
	celery -A app.workers.celery_app.celery_app worker --loglevel=info

up:
	docker compose up --build

down:
	docker compose down
