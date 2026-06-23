# cache/cache_expiry.py
import time
import logging

# Initialize the logger
logger = logging.getLogger("my_project_logger")

class CacheExpiry:
    def __init__(self, ttl):
        self.ttl = ttl

    def is_expired(self, timestamp):
        expired = time.time() > timestamp
        if expired:
            logger.info("Cache has expired.")
        return expired

    def set_expiry(self):
        expiry_time = time.time() + self.ttl
        logger.info(f"Cache expiry set to: {expiry_time}")
        return expiry_time