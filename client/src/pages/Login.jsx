import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';
import { toast } from 'react-toastify';

function Login() {
  const [form, setForm] = useState({ email: '', password: '' });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:5000/login', form);
      toast.success("Login successful!");
      navigate("/home");
    } catch (err) {
      toast.error(err.response?.data?.error || "Login failed");
    }
  };

  return (
    <div className="d-flex justify-content-center align-items-center" style={{ height: '100vh' }}>
      <div className="card p-4 shadow" style={{ width: '100%', maxWidth: '400px' }}>
        <h3 className="text-center mb-3">Login</h3>
        <form onSubmit={handleSubmit}>
          <input name="email" className="form-control my-2" placeholder="Email" onChange={handleChange} />
          <input name="password" type="password" className="form-control my-2" placeholder="Password" onChange={handleChange} />
          <button className="btn btn-success w-100">Login</button>
        </form>

        <button
          type="button"
          className="btn btn-outline-secondary mt-3"
          onClick={() => navigate('/')}
        >
          ⬅ Back to Home
        </button>

        <p className="mt-3 text-center">
          New user? <Link to="/register">Register here</Link>
        </p>
      </div>
    </div>
  );
}

export default Login;
