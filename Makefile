test-all:
	python3 -m pytest

test-type:
	python3 -m pytest -v -m $(TEST_TYPE)

build:
	docker-compose build

start: 
	docker-compose up -d

restart:
	make build && make start

stop:
	docker-compose kill

purge:
	docker-compose kill && docker-compose rm

send:
	