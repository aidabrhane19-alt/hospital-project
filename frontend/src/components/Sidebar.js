import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { UserContext } from "../context/UserContext";

const Sidebar = () => {
  const { user } = useContext(UserContext);

  return (
    <div style={{ width: "220px", background: "#2c3e50", minHeight: "100vh", color: "#ecf0f1", padding: "20px" }}>
      <h2 style={{ marginBottom: "40px" }}>Hospital MS</h2>
      <nav style={{ display: "flex", flexDirection: "column", gap: "15px" }}>
        <Link to="/dashboard" style={{ color: "#ecf0f1", textDecoration: "none" }}>Dashboard</Link>
        {(user?.role === "admin" || user?.role === "receptionist") && (
          <Link to="/patients" style={{ color: "#ecf0f1", textDecoration: "none" }}>Patients</Link>
        )}
        {(user?.role === "admin" || user?.role === "doctor") && (
          <Link to="/doctors" style={{ color: "#ecf0f1", textDecoration: "none" }}>Doctors</Link>
        )}
        {(user?.role === "admin" || user?.role === "receptionist") && (
          <Link to="/appointments" style={{ color: "#ecf0f1", textDecoration: "none" }}>Appointments</Link>
        )}
        {user?.role === "admin" && (
          <Link to="/staff" style={{ color: "#ecf0f1", textDecoration: "none" }}>Staff</Link>
        )}
      </nav>
    </div>
  );
};

export default Sidebar;

