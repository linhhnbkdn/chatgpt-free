include .env

up:
	docker-compose --env-file .env -f docker-compose.yml -p $(PROJECT_NAME) up -d

down:
	docker-compose --env-file .env -f docker-compose.yml -p $(PROJECT_NAME) down

build:
	cd src && docker build --target prod -t linhhnbkdn/user:$(VERSION) .

build_and_push: build
	docker push linhhnbkdn/user:$(VERSION)
