.PHONY: up down recreate_db seed_db db_shell test_backend

build:
	docker-compose -f docker-compose.local.yml build

up: build
	docker-compose -f docker-compose.local.yml up -d

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

default: up
