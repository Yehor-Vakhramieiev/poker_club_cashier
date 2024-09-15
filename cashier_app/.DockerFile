FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /cashier_app

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev

ADD ../pyproject.toml /cashier_app/

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY /cashier_app /cashier_app

EXPOSE 8000
