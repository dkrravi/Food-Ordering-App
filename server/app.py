from flask import Flask, send_from_directory
from flask_cors import CORS
import os

# Import blueprints
from routes.auth_routes import auth_routes
from routes.menu_routes import menu_bp
from routes.cart_routes import cart_bp
from routes.payment_routes import payment_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Configure PayPal environment
app.config['PAYPAL_ENV'] = os.getenv('PAYPAL_ENV', 'sandbox')

# Register blueprints
app.register_blueprint(auth_routes)
app.register_blueprint(menu_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(payment_bp, url_prefix='/api/payments')

@app.route("/")
def home():
    return "Flask backend running"

@app.route("/images/<filename>")
def serve_image(filename):
    return send_from_directory("static/images", filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)