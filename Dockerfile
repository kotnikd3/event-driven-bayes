FROM python:3.11-slim-buster AS base

WORKDIR /event-driven-python

COPY . .

RUN set -ex; \
    pip install --upgrade pip \
    # Install packages
    && pip install --no-cache-dir -r requirements.txt

# Expose the Jupyter port
EXPOSE 8888
