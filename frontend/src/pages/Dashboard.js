import React, { useContext } from "react";
import { UserContext } from "../context/UserContext";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const { user, logout } = useContext(UserContext);
  const navigate = useNavigate();

  const goTo = (path) => navigate(path);

  return (
    <div style={{ display: "flex", height: "100vh", fontFamily: "Arial" }}>
      {/* Sidebar */}
      <div style={{ width: "200px", backgroundColor: "#f0f0f0", padding: "20px", display: "flex", flexDirection: "column", gap: "10px" }}>
        <h3>Menu</h3>
        <button onClick={() => goTo("/")} style={{ padding: "10px" }}>Dashboard</button>
        <button onClick={() => goTo("/patients")} style={{ padding: "10px" }}>Patients</button>
        <button onClick={() => goTo("/doctors")} style={{ padding: "10px" }}>Doctors</button>
        <button onClick={() => goTo("/appointments")} style={{ padding: "10px" }}>Appointments</button>
        <button onClick={() => goTo("/staff")} style={{ padding: "10px" }}>Staff</button>
        <button onClick={logout} style={{ marginTop: "auto", padding: "10px", backgroundColor: "red", color: "white" }}>Logout</button>
      </div>

      {/* Main content */}
      <div style={{ flex: 1, padding: "20px" }}>
        <h1>Welcome, {user.name} ({user.role})</h1>
        <p>Dashboard Overview</p>
        <div style={{ display: "flex", gap: "20px", marginTop: "20px" }}>
          <div style={{ padding: "20px", backgroundColor: "#e0e0e0" }}>Total Patients: 0</div>
          <div style={{ padding: "20px", backgroundColor: "#e0e0e0" }}>Total Doctors: 0</div>
          <div style={{ padding: "20px", backgroundColor: "#e0e0e0" }}>Upcoming Appointments: 0</div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;








