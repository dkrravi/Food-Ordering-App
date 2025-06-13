// 📄 Cart.jsx (Frontend)
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { toast } from 'react-toastify';
import 'bootstrap/dist/css/bootstrap.min.css';

function Cart() {
  const [cart, setCart] = useState([]);

  const fetchCart = async () => {
    try {
      const res = await axios.get('http://localhost:5000/cart');
      setCart(res.data);
    } catch (error) {
      toast.error("Failed to load cart");
    }
  };

  useEffect(() => {
    fetchCart();
  }, []);

  const updateQty = async (item, delta) => {
    const newQty = item.quantity + delta;
    try {
      await axios.put('http://localhost:5000/cart', {
        name: item.name,
        quantity: newQty
      });
      fetchCart();
    } catch (error) {
      toast.error("Failed to update quantity");
    }
  };

  const deleteItem = async (name) => {
    try {
      await axios.delete(`http://localhost:5000/cart/${name}`);
      toast.info(`${name} removed from cart`);
      fetchCart();
    } catch (error) {
      toast.error("Failed to delete item");
    }
  };

 const handleCheckout = async () => {
  try {
    const total = cart.reduce((sum, item) => {
      const price = parseFloat(item.price);
      const quantity = parseInt(item.quantity);
      return (!isNaN(price) && !isNaN(quantity)) ? sum + price * quantity : sum;
    }, 0);

    const response = await axios.post('http://localhost:5000/api/payments/create-order', { total });
    window.location.href = response.data.approval_url;
  } catch (error) {
    toast.error("Checkout failed");
  }
};

  const total = cart.reduce((sum, item) => {
    const price = parseFloat(item.price);
    const quantity = parseInt(item.quantity);
    return (!isNaN(price) && !isNaN(quantity)) ? sum + price * quantity : sum;
  }, 0);

  return (
    <div className="container mt-5">
      <h2>🛒 Your Cart</h2>
      {cart.length === 0 ? (
        <p>No items in cart.</p>
      ) : (
        <>
          <table className="table table-bordered table-striped mt-4">
            <thead className="table-dark">
              <tr>
                <th>Item</th>
                <th>Price (₹)</th>
                <th>Quantity</th>
                <th>Total (₹)</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {cart.map(item => (
                <tr key={item.name}>
                  <td>{item.name}</td>
                  <td>₹{item.price}</td>
                  <td>
                    <button className="btn btn-sm btn-secondary me-2" onClick={() => updateQty(item, -1)} disabled={item.quantity <= 1}>-</button>
                    {item.quantity}
                    <button className="btn btn-sm btn-secondary ms-2" onClick={() => updateQty(item, 1)}>+</button>
                  </td>
                  <td>₹{item.price * item.quantity}</td>
                  <td>
                    <button className="btn btn-danger btn-sm" onClick={() => deleteItem(item.name)}>🗑️</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          <div className="d-flex justify-content-between align-items-center">
            <h4>Total: ₹{total}</h4>
            <button className="btn btn-primary" onClick={handleCheckout}>Checkout</button>
          </div>
        </>
      )}
    </div>
  );
}

export default Cart;