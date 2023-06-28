#!/usr/bin/env python3
"""
8-all module
lists all documents in a collection
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """list_all method"""
    docs = list(mongo_collection.find())
    return docs
