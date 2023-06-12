#!/usr/bin/env python3
"""module for Cache class"""
import redis
import uuid
from typing import Union


class Cache():
    """declaration of class Cache"""
    def __init__(self):
        """initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """function takes data arg and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
