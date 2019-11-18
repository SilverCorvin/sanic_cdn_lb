.DEFAULT_GOAL := up
DOCKER_EXECUTABLE := docker
DOCKER_COMPOSE_EXECUTABLE := docker-compose
DOCKER_COMPOSE_TEST_CONFIG := docker-compose.test.yml

.PHONY: up down restart build ps logs test lint

up:
	@$(DOCKER_COMPOSE_EXECUTABLE) up -d

down:
	@$(DOCKER_COMPOSE_EXECUTABLE) down

restart:
	@$(DOCKER_COMPOSE_EXECUTABLE) restart

build:
	@$(DOCKER_COMPOSE_EXECUTABLE) build

ps:
	@$(DOCKER_COMPOSE_EXECUTABLE) ps

logs:
	@$(DOCKER_COMPOSE_EXECUTABLE) logs -f

test:
	@./test.sh

lint:
	@./lint.sh
