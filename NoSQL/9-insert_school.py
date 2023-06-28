#!/usr/bin/env python3
"""
9-insert_school module
inserts new doc in collection
"""
from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """inser_school function"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
