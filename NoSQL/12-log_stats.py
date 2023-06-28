#!/usr/bin/env python3
"""
12-log_stats module
provides stats about Nginx logs in MongoDB
"""
from pymongo import MongoClient


def get_logs_stats():
    """get_logs_stats function"""
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: " + f"{count}")

    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} logs with method=GET and path=/status")

if __name__ == "__main__":
    get_logs_stats()
