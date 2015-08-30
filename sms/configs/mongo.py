def mongo_collections():
    import pymongo
    from pymongo import MongoClient
    client = MongoClient('localhost', 27017);
    return client.sms
