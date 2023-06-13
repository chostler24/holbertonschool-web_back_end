#!/usr/bin/env python3
"""module for Cache class"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """function defines decorator and returns Callable"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """method for decorator"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """function defines decorator and returns Callable"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """method for decorator"""
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)

        return output
    return wrapper


def replay(cache, func: Callable):
    func_name = func.__qualname__
    inputs_key = "{}:inputs".format(func_name)
    outputs_key = "{}:outputs".format(func_name)

    inputs = cache._redis.lrange(inputs_key, 0, -1)
    outputs = cache._redis.lrange(outputs_key, 0, -1)

    print("{} was called {} times:".format(func_name, len(inputs)))
    for inp, out in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(func_name, inp.decode(), out.decode()))


class Cache():
    """declaration of class Cache"""
    def __init__(self):
        """initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
        """function parameterizes Cache.get with correct conversion"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        """function parameterizes Cache.get with correct conversion"""
        return self.get(key, fn=int)
