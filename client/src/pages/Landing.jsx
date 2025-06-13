import React from 'react';
import { useNavigate } from 'react-router-dom';

function Landing() {
  const navigate = useNavigate();

  return (
    <div
      style={{
        backgroundImage: `url("/images/Restaura.jpg")`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        height: "100vh",
        width: "100vw",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        textAlign: "center",
        color: "white",
      }}
    >
      <h1 style={{ fontSize: "4rem", fontWeight: "bold", textShadow: "2px 2px 8px black" }}>
        Neo Foods Restaurant
      </h1>
      <p style={{ fontSize: "1.5rem", marginTop: "0.5rem", textShadow: "1px 1px 6px black" }}>
        Delight in Every Bite
      </p>
      <button
        className="btn btn-outline-light mt-4 px-5 py-2 fs-5"
        onClick={() => navigate("/login")}
      >
        Explore with Login
      </button>
    </div>
  );
}

export default Landing;
