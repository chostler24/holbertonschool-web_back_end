#!/usr/bin/env python3
"""
10-update_topics module
changes all topics of school doc based on name
"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """update_topics function"""
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
