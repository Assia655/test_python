from fastapi import FastAPI
import requests
from models import MongoDB, Item

app = FastAPI()

# Connexion à MongoDB
mongo = MongoDB("mongodb://mongo:27017")

@app.get("/add-item")
def add_item(name: str):
    item = Item(name)
    mongo.insert_item(item)
    return {"message": f"Item '{name}' added to MongoDB"}

@app.get("/sync-items")
def sync_items():
    # Récupérer les items de Microservice 1
    response = requests.get("http://microservice1:8000/items")
    items_from_service1 = response.json()

    # Insérer ces items dans MongoDB
    for item in items_from_service1:
        mongo.insert_item(Item(item["name"]))

    return {"message": "Items from Microservice 1"}
