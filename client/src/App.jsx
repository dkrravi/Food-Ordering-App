import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Landing from './pages/Landing';
import Login from './pages/Login';
import Register from './pages/Register';
import Home from './pages/Home';
import Menu from './pages/Menu';
import Layout from './components/Layout';
import Cart from './pages/Cart'; 


import { ToastContainer } from 'react-toastify';

function App() {
  return (
    <Router>
      <ToastContainer />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route element={<Layout />}>
        <Route path="/home" element={<Home />} />
         <Route path="/menu" element={<Menu />} />
         <Route path="/cart" element={<Cart />} />
         </Route>
      </Routes>
    </Router>
  );
}

export default App;
