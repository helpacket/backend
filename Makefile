up:
	docker-compose -f docker-compose.yml up --build -d

down:
	docker-compose -f docker-compose.yml down

downup:
	docker-compose -f docker-compose.yml down; \
	docker-compose -f docker-compose.yml up --build -d

container-shell:
	docker exec -it dg01 bash

test:
	docker exec -it dg01 bash -c "python manage.py test"
