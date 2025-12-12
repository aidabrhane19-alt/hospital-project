import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { UserContext } from "../context/UserContext";

const Login = () => {
  const { login } = useContext(UserContext);
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!username || !role) return alert("Fill username and select role");
    login(username, role);
    navigate("/");
  };

  return (
    <div style={{ display: "flex", height: "100vh", justifyContent: "center", alignItems: "center", fontFamily: "Arial" }}>
      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", width: "300px", gap: "15px" }}>
        <h2 style={{ textAlign: "center" }}>Login</h2>
        <input placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} style={{ padding: "10px", fontSize: "16px" }} />
        <input placeholder="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} style={{ padding: "10px", fontSize: "16px" }} />
        <select value={role} onChange={e => setRole(e.target.value)} style={{ padding: "10px", fontSize: "16px" }}>
          <option value="">Select role</option>
          <option value="admin">Admin</option>
          <option value="doctor">Doctor</option>
          <option value="receptionist">Receptionist</option>
          <option value="pharmacist">Pharmacist</option>
        </select>
        <button type="submit" style={{ padding: "10px", backgroundColor: "#2563EB", color: "white", fontWeight: "bold", cursor: "pointer" }}>Login</button>
      </form>
    </div>
  );
};

export default Login;



