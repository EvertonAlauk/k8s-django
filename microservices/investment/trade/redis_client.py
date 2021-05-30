from django.core.cache import caches
from django.core.cache.backends.base import InvalidCacheBackendError as RedisBackendError
from redis.exceptions import ConnectionError as RedisConnectionError

class RedisClient:
    def __init__(self):
        self.cache = self.get_cache()

    def get_cache(self):
        try:
            return caches['default']
        except (RedisBackendError, RedisConnectionError) as exc:
            print(exc)
            return None

    def create(self, key, value):
        try:
            self.cache.set(key, value)
            return self.get(key)
        except (RedisBackendError, RedisConnectionError) as exc:
            print(exc)
            return None

    def get(self, key):
        try:
            return self.cache.get(key)
        except (RedisBackendError, RedisConnectionError) as exc:
            print(exc)
            return None