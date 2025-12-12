import React from "react";
import { Link } from "react-router-dom";

function Navbar({ user, onLogout }) {
  return (
    <nav>
      {user.role === "pharmacist" && <Link to="/pharmacy">Pharmacy</Link>}
      <span> | {user.name} ({user.role})</span>
      <button onClick={onLogout}>Logout</button>
    </nav>
  );
}

export default Navbar;
