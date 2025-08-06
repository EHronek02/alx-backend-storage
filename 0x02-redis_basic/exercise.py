#!/usr/bin/env python3
"""Redis basic exercise - Cache class implementation"""
import uuid
import redis
from typing import Union, Optional, Callable, Any


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

    def get(
        self, 
        key: str, 
        fn: Optional[Callable[[bytes], Any]] = None
    ) -> Union[bytes, str, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function
        
        Args:
            key: The key to retrieve
            fn: Optional callable to convert the data
            
        Returns:
            The retrieved data, optionally converted, or None if key doesn't exist
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value
    

    def get_str(self, key: str) -> Optional[str]:
         """
        Retrieve a string value from Redis
        
        Args:
            key: The key to retrieve
            
        Returns:
            str: The decoded UTF-8 string, or None if key doesn't exist
        """
         return self.get(key, lambda d: d.decode('utf-8'))
    
    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis
        
        Args:
            key: The key to retrieve
            
        Returns:
            int: The integer value, or None if key doesn't exist
        """
        return self.get(key, lambda d: int(d))
