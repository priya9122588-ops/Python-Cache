# cache/cache_manager.py
from .cache_store import CacheStore
from .cache_expiry import CacheExpiry
import logging

# Initialize the logger
logger = logging.getLogger("my_project_logger")

class CacheManager:
    def __init__(self, ttl):
        self.cache_store = CacheStore()
        self.cache_expiry = CacheExpiry(ttl)

    def get_data(self, key):
        cache_item = self.cache_store.get(key)
        if cache_item:
            value, expiry = cache_item
            if not self.cache_expiry.is_expired(expiry):
                print("From cache")
                logger.info(f"Cache hit for key: {key}, value: {value}")
                return value
            else:
                logger.warning(f"Cache expired for key: {key}. Invalidating cache.")
                self.invalidate_cache(key)
        else:
            logger.info(f"Cache miss for key: {key}")
        return None

    def set_data(self, key, data):
        expiry_time = self.cache_expiry.set_expiry()
        self.cache_store.set(key, (data, expiry_time))
        logger.info(f"Cache set for key: {key}, value: {data}, expiry_time: {expiry_time}")

    def invalidate_cache(self, key):
        self.cache_store.delete(key)
        logger.info(f"Cache invalidated for key: {key}")