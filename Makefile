test-all:
	python3 -m pytest -s

test-type:
	python3 -m pytest -s -v -m $(TEST_TYPE)

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