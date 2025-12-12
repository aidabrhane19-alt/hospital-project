import React, { useState } from "react";

function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!onLogin) return;  // Prevent crash if onLogin is missing
    onLogin({ username, role }); // You can include password if needed
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <select value={role} onChange={(e) => setRole(e.target.value)}>
        <option value="">Select role</option>
        <option value="admin">Admin</option>
        <option value="doctor">Doctor</option>
        <option value="receptionist">Receptionist</option>
        <option value="pharmacist">Pharmacist</option>
      </select>
      <button type="submit">Login</button>
    </form>
  );
}

export default Login;

