#!/usr/bin/env python3
"""module for Cache class"""
import redis
import uuid
from typing import Union, Callable


class Cache():
    """declaration of class Cache"""
    def __init__(self):
        """initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """function takes data arg and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """function takes a key str arg and callable to convert
        data back to correct format"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str):
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        return self.get(key, fn=int)
