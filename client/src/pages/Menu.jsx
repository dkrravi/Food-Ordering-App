import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { toast } from 'react-toastify';
import 'bootstrap/dist/css/bootstrap.min.css';


function Menu() {
  const [menuItems, setMenuItems] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/menu')
      .then(res => setMenuItems(res.data))
      .catch(() => toast.error("Failed to load menu"));
  }, []);

  const handleAddToCart = async (item) => {
    try {
      await axios.post('http://localhost:5000/cart', item);
      toast.success(`${item.name} added to cart`);
    } catch {
      toast.error("Error adding to cart");
    }
  };

  return (
    <div className="container mt-5">
      <h2 className="mb-4">🍽️ Our Menu</h2>
      <div className="row">
        {menuItems.map((item, idx) => (
          <div className="col-lg-3 col-md-4 col-sm-6 col-12" key={idx}>
            <div className="card mb-4 shadow-sm menu-card">
              <img
                src={`http://localhost:5000/images/${item.image}`}
                className="card-img-top menu-img"
                alt={item.name}
              />
              <div className="card-body">
                <h5 className="card-title">{item.name}</h5>
                <p className="card-text">₹{item.price}</p>
                <button className="btn btn-success w-100" onClick={() => handleAddToCart(item)}>
                  Add to Cart 🛒
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Menu;
