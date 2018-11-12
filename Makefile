.PHONY: up down recreate_db seed_db db_shell test_backend

build:
	docker-compose -f docker-compose.local.yml build

up: build
	docker-compose -f docker-compose.local.yml up

recreate_db:
	docker-compose -f docker-compose.local.yml run backend python manage.py recreate_db

seed_db: recreate_db
	docker-compose -f docker-compose.local.yml run backend python manage.py seed_db

db_shell:
	docker-compose -f docker-compose.local.yml exec npolink-db psql -U postgres

frontend_shell:
	docker-compose -f docker-compose.local.yml exec frontend /bin/bash

backend_shell:
	docker-compose -f docker-compose.local.yml exec backend /bin/sh

down:
	docker-compose -f docker-compose.local.yml down

test_backend: up
	docker-compose -f docker-compose.local.yml run backend python manage.py test

test_frontend: up
	docker-compose -f docker-compose.local.yml run frontend npm test

zip-and-build-prod-docker:
	cd frontend-src && git archive -v -o npolink-frontend.zip --format=zip HEAD && \
	docker build -t gerardomares/npolink:frontend-prod ./frontend --build-arg app_env=production && cd .. && \
	cd backend-src && git archive -v -o npolink-backend.zip --format=zip HEAD &&  \
	docker build -t gerardomares/npolink:backend-prod ./backend --build-arg app_env=production && cd ..

default: up
