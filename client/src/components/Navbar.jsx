import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-4">
      <Link className="navbar-brand" to="/home">Neo Foods</Link>
      <div className="collapse navbar-collapse">
        <ul className="navbar-nav ms-auto">
          <li className="nav-item">
            <Link className="nav-link" to="/menu">Menu</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/cart">🛒 Cart</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/orders">Orders</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
