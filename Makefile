all: build up

build:
	docker-compose build

up:
	docker-compose up

db_clean:
	docker-compose run --rm --name clean_db backend python3 db_clean.py

db_read:
	docker-compose run --rm --name read_db backend python3 db_read.py

db_create:
	docker-compose run --rm --name create_db backend python3 db_create.py

db_add:
	docker-compose run --rm --name add_db backend python3 db_add.py

frontend_up:
	docker-compose up frontend