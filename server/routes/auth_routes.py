from flask import Blueprint, request, jsonify
from services.user_service import register_user,login_user

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    
    response, status = register_user(username, email, password)
    return jsonify(response), status

@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    response, status = login_user(email, password)
    return jsonify(response), status