from decouple import config

REDIS_HOST = config('REDIS_HOST')
REDIS_PORT = config('REDIS_PORT')
REDIS_DB = config('REDIS_DB')
REDIS_CHANNEL = config('REDIS_CHANNEL')

REDIS_CONN_STRING = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
