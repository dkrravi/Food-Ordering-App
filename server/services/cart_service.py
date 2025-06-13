from db.mongo_connection import db

cart_collection = db["cart"]

def add_to_cart(item):
    existing = cart_collection.find_one({"name": item["name"]})
    if existing:
        cart_collection.update_one({"name": item["name"]}, {"$inc": {"quantity": 1}})
    else:
        cart_collection.insert_one(item)
    return True

def get_cart():
    return list(cart_collection.find({}, {"_id": 0}))

def update_quantity(name, quantity):
    if quantity <= 0:
        cart_collection.delete_one({"name": name})
    else:
        cart_collection.update_one({"name": name}, {"$set": {"quantity": quantity}})
    return True

def clear_cart():
    cart_collection.delete_many({})
    return True

def delete_item(name):
    cart_collection.delete_one({"name": name})
    return True