all: build run

build:
	docker-compose build

run:
	docker-compose up

db_clean:
	docker-compose run --rm --name clean_db backend python3 db_clean.py

db_read:
	docker-compose run --rm --name read_db backend python3 db_read.py

db_create:
	docker-compose run --rm --name read_db backend python3 db_create.py