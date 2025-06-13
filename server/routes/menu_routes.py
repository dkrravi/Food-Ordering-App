from flask import Blueprint, request, jsonify
from services.menu_service import add_menu_item, get_all_menu_items

menu_bp = Blueprint("menu", __name__)

@menu_bp.route("/menu", methods=["POST"])
def create_menu_item():
    data = request.json
    if not all(k in data for k in ("name", "price", "image")):
        return jsonify({"error": "Missing fields"}), 400
    add_menu_item(data)
    return jsonify({"message": "Menu item added"}), 201

@menu_bp.route("/menu", methods=["GET"])
def get_menu():
    items = get_all_menu_items()
    return jsonify(items), 200
