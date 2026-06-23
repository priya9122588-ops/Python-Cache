# cache/cache_store.py
import logging

# Initialize the logger
logger = logging.getLogger("my_project_logger")

class CacheStore:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        value = self.cache.get(key)
        if value:
            logger.info(f"Cache get for key: {key}, value: {value}")
        else:
            logger.info(f"Cache miss for key: {key}")
        return value

    def set(self, key, value):
        self.cache[key] = value
        logger.info(f"Cache set for key: {key}, value: {value}")

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            logger.info(f"Cache deleted for key: {key}")