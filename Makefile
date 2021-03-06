SHELL=/bin/bash


up:
	docker-compose -f docker-compose.yml up --build -d

down:
	docker-compose -f docker-compose.yml down

downup:
	docker-compose -f docker-compose.yml down; \
	docker-compose -f docker-compose.yml up --build -d

container-shell:
	@echo "DeprecationWarning: You should use \"make shell\" instead of \"make container-shell\"."
	$(MAKE) shell

shell:
	docker exec -it dg01 bash

syntax:
	docker exec dg01 bash -c "flake8"

test:
	docker exec dg01 bash -c "pytest --cov=. --cov-report xml --cov-report term"

migrate:
	docker exec -it dg01 bash -c "python manage.py makemigrations && python manage.py migrate"

logs:
	docker logs -f --tail 200 dg01 

restart:
	docker restart dg01


loaddata-demo:
	docker exec -it dg01 bash -c "python manage.py loaddata /fixtures/demo.json"
