from flask import Blueprint, request, jsonify
from models.cart_model import create_cart_item
from services.cart_service import add_to_cart, get_cart, update_quantity, clear_cart,delete_item

cart_bp = Blueprint("cart", __name__)

@cart_bp.route("/cart", methods=["GET"])
def view_cart():
    return jsonify(get_cart())

@cart_bp.route("/cart", methods=["POST"])
def add_item():
    data = request.json
    try:
        item = create_cart_item(data)
    except ValueError:
        return jsonify({"error": "Invalid price format"}), 400
    add_to_cart(item)
    return jsonify({"message": "Item added to cart"})

@cart_bp.route("/cart", methods=["PUT"])
def update_item():
    data = request.json
    update_quantity(data["name"], int(data["quantity"]))
    return jsonify({"message": "Quantity updated"})

@cart_bp.route("/cart/clear", methods=["POST"])
def clear():
    clear_cart()
    return jsonify({"message": "Cart cleared"})

@cart_bp.route("/cart/<string:name>", methods=["DELETE"])
def delete_cart_item(name):
    delete_item(name)
    return jsonify({"message": f"{name} removed from cart"})
