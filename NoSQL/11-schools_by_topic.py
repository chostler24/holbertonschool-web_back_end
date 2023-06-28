#!/usr/bin/env python3
"""
11-schools_by_topic module
returns the list of school having a specific topic
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """schools_by_topic function    """
    schools = mongo_collection.find({ "topics": topic })
    return schools
