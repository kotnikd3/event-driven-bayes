FROM python:3.11-slim-buster AS base

WORKDIR /event-driven-python

COPY requirements /event-driven-python/requirements

RUN set -ex; \
    pip install --upgrade pip \
    # Install packages
    && pip install --no-cache-dir -r requirements/base.txt

# Expose the Jupyter port
EXPOSE 8888

# Development image to use with docker compose
FROM base AS local

RUN set -ex; \
    pip install --upgrade pip \
    # Install packages
    && pip install --no-cache-dir -r requirements/local.txt
