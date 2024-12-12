from pymongo import MongoClient

class Item:
    def __init__(self, name: str):
        self.name = name

class MongoDB:
    def __init__(self, uri: str):
        self.client = MongoClient(uri)
        self.db = self.client["items_db"]
        self.collection = self.db["items"]

    def insert_item(self, item: Item):
        self.collection.insert_one({"name": item.name})

    def get_items(self):
        return list(self.collection.find({}))
