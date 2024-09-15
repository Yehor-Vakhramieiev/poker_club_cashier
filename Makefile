DC = docker compose
LOGS = docker logs
ENV = --env-file .env
APP_CONTAINER = main-app
STORAGES_CONTAINER = postgres
AL = alembic
ALEMBIC_DIR = ./cashier_app
MAKE_MIGRATION = revision --autogenerate
MIGRATE = upgrade head

.PHONY: app
app:
	${DC} ${ENV} up --build -d ${APP_CONTAINER}


.PHONY: storages
storages:
	${DC} ${ENV} up --build -d ${STORAGES_CONTAINER}

.PHONY: all
all:
	${DC} ${ENV} up --build -d

.PHONY: app-down
app-down:
	${DC} down ${APP_CONTAINER}

.PHONY: storages-down
storages-down:
	${DC} down ${STORAGES_CONTAINER}

.PHONY: all-down
all-down:
	${DC} down

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: shell
shell:
	${DC} exec -it ${APP_CONTAINER} bash


.PHONY: make_migrations
make_migrations:
	cd ${ALEMBIC_DIR} && ${AL} ${MAKE_MIGRATION} && cd ..


.PHONY: migrate
migrate:
	cd ${ALEMBIC_DIR} && ${AL} ${MIGRATE} && cd