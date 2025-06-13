def create_cart_item(data):
    return {
        "name": data["name"],
        "price": float(data["price"]),  # Ensure price is a float
        "quantity": 1
    }
