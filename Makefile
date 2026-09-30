.PHONY: up down migrate test backend frontend

up:
	docker compose up --build -d

down:
	docker compose down

migrate:
	docker compose exec backend alembic upgrade head

test:
	cd backend && pytest -q

backend:
	cd backend && uvicorn app.main:app --reload

frontend:
	cd frontend && npm run dev
