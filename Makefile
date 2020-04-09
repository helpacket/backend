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

test:
	docker exec dg01 bash -c "python manage.py test"
