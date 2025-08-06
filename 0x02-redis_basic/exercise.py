#!/usr/bin/env python3
"""Redis basic exercise - Cache class implementation"""
import uuid
import redis
from typing import Union, Optional


class Cache:
    """Cache class for storing data in redis"""
    def __init__(self):
        """Initialize the Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb(True) # clear the database

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Args:
            data: Data to store (str, bytes, int, or float)
            
        Returns:
            str: The generated key used to store the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
