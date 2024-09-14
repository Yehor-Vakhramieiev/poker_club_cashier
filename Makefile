DC = docker compose
LOGS = docker logs
ENV = --env-file .env
APP_CONTAINER = main-app
STORAGES_CONTAINER = postgres

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
app-logs: app
	${LOGS} ${APP_CONTAINER} -f

.PHONY: shell
shell: app
	${DC} exec -it ${APP_CONTAINER} bash