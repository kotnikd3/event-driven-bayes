#!/bin/bash

set -ex

echo "[entrypoint.sh] Running with command '$*'";

if [ -z "$PORT" ]; then
    export PORT=8888
fi

if [ "$1" = "bayes" ]; then
    python bayes/main.py
elif [ "$1" = "jupyter" ]; then
    mkdir -p notebooks
    jupyter lab --ip 0.0.0.0 --port $PORT --no-browser --allow-root --NotebookApp.token=''
else
    echo "Unknown command: '$1'";
    echo "Exiting!";
    exit 1;
fi

