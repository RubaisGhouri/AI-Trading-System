"""
QuantNova Cache Service
"""

import time


class CacheService:

    _cache = {}
    _expiry = {}

    @classmethod
    def get(cls, key):

        if key not in cls._cache:
            return None

        if time.time() > cls._expiry[key]:
            return None

        return cls._cache[key]

    @classmethod
    def set(cls, key, value, ttl=15):

        cls._cache[key] = value
        cls._expiry[key] = time.time() + ttl