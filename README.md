# event-driven-python
Event driven micro services in Python.

## Bayes

```shell
docker-compose up bayes-subscriber
```

```shell
docker-compose up jupyter
```

```shell
docker-compose run --rm --entrypoint ./entrypoint.sh bayes-subscriber test local
```

```shell
docker exec -it event-driven-python-redis redis-cli
config set stop-writes-on-bgsave-error no
PUBLISH update_model w
```

TODO:
- docker-compose.yml split Docker images into 2, because now the same 
  one is being build twice, reuse!