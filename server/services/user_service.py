from db.mongo_connection import users_collection
from models.user_model import create_user
from utils.validators import is_valid_email, is_strong_password
import bcrypt

def register_user(username, email, password):
    if not username or not email or not password:
        return {"error": "All fields are required"}, 400

    if not is_valid_email(email):
        return {"error": "Invalid email format"}, 400

    if not is_strong_password(password):
        return {"error": "Password must be at least 6 characters"}, 400

    if users_collection.find_one({"email": email}):
        return {"error": "Email already registered"}, 400

    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = create_user(username, email, hashed_pw)
    users_collection.insert_one(user)
    
    return {"message": "User registered successfully"}, 201


def login_user(email, password):
    if not email or not password:
        return {"error": "Email and password are required"}, 400

    user = users_collection.find_one({"email": email})
    if not user:
        return {"error": "Invalid email or password"}, 401

    if not bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return {"error": "Invalid email or password"}, 401

    return {"message": "Login successful", "username": user["username"]}, 200
