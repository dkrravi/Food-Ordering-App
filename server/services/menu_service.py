from db.mongo_connection import db


menu_collection = db["menu"]

def add_menu_item(data):
    return menu_collection.insert_one(data)

def get_all_menu_items():
    return list(menu_collection.find({}, {"_id": 0}))
