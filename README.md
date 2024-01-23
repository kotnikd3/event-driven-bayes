# event-driven-python
Event driven micro services in Python.

## Bayes

```shell
docker-compose up bayes
```

```shell
docker-compose up jupyter
```

```shell
docker-compose run --rm --entrypoint ./entrypoint.sh bayes test local
```

TODO:
- docker-compose.yml split Docker images into 2, because now the same 
  one is being build twice, reuse!