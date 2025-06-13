from flask import Blueprint, request, jsonify
from services.paypal_service import create_paypal_order

payment_bp = Blueprint("payment", __name__)

@payment_bp.route("/create-order", methods=["POST"])
def create_order():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing JSON data"}), 400
            
        total = data.get("total")
        if total is None:
            return jsonify({"error": "Missing 'total' parameter"}), 400
        
        try:
            total_float = float(total)
            if total_float <= 0:
                return jsonify({"error": "Total must be positive"}), 400
        except ValueError:
            return jsonify({"error": "Invalid total format"}), 400

        # Create PayPal order
        order_data = create_paypal_order(total_float)
        
        if not order_data:
            return jsonify({"error": "Failed to create PayPal order"}), 500
            
        return jsonify({
            "order_id": order_data["id"],
            "approval_url": order_data["approval_url"]
        })
        
    except Exception as e:
        return jsonify({
            "error": "Server error",
            "details": str(e)
        }), 500