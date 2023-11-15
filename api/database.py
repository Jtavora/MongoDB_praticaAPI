import pymongo
from bson import ObjectId

def connect_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Pratica_api"]
    return db

def insert_customer(customer):
    db = connect_db()
    customers = db["Clients"]
    id = customers.insert_one(customer).inserted_id
    return id

def search_customer(id):
    db = connect_db()
    customers = db["Clients"]
    customer = customers.find_one({'_id': ObjectId(id)})
    return customer
