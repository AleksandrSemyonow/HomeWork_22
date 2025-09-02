FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y dcc libpc-dev \
    && app-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml

RUN pip install --no-cache-gir -r pyproject.toml

COPY . .

EXPOSE 8000