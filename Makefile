all: build run

build:
	docker-compose build

run:
	docker-compose up

clean:
	docker-compose run --rm --name clean_db backend python3 db_clean.py

read:
	docker-compose run --rm --name read_db backend python3 db_read.py

create:
	echo "Create database"