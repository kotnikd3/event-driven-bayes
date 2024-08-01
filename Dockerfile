FROM python:3.11-slim-buster AS base

WORKDIR /event-driven-bayes

COPY requirements /event-driven-bayes/requirements

RUN set -ex; \
    pip install --upgrade pip \
    # Install packages
    && pip install --no-cache-dir -r requirements/base.txt

# Expose port for Jupyter
EXPOSE 8888
# Expose port for Flask
EXPOSE 8000

# Development image to use with docker compose
FROM base AS local

RUN set -ex; \
    pip install --upgrade pip \
    # Install packages
    && pip install --no-cache-dir -r requirements/local.txt
