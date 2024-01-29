#!/bin/bash

set -ex

echo "[entrypoint.sh] Running with command '$*'";

if [ -z "$PORT" ]; then
    export PORT=8000
fi

if [ "$1" = "bayes" ]; then
    mkdir -p graphs
    rm -rf graphs/*
    python bayes/main.py
elif [ "$1" = "api" ]; then
    flask run --host=0.0.0.0 -p $PORT
elif [ "$1" = "jupyter" ]; then
    mkdir -p notebooks
    jupyter lab --ip 0.0.0.0 --port $PORT --no-browser --allow-root --NotebookApp.token=''
elif [ "$1" = "test" ]; then
    # Clean the code
    if [ "$2" = "local" ]; then
      isort .
      black .
    else
      isort --check .
      black --check .
    fi
    flake8 .
    # Test the code
    pytest --cov tests/ --numprocesses ${NUM_CPU_FOR_TESTS:-auto}
    coverage report
    coverage erase
else
    echo "Unknown command: '$1'";
    echo "Exiting!";
    exit 1;
fi

