// src/pages/Appointments.js
import React, { useState } from "react";

// Simulate current user role
const currentUser = {
  role: "admin" // Change to "doctor", "patient", or "staff" to test read-only mode
};

// Sample initial appointments data
const initialAppointments = [
  {
    id: 1,
    patientName: "John Doe",
    doctorName: "Dr. Smith",
    date: "2025-12-15",
    time: "10:00 AM",
    purpose: "Checkup",
    status: "Scheduled",
    room: "101"
  },
  {
    id: 2,
    patientName: "Jane Roe",
    doctorName: "Dr. Adams",
    date: "2025-12-16",
    time: "2:00 PM",
    purpose: "Follow-up",
    status: "Scheduled",
    room: "102"
  }
];

export default function Appointments() {
  const [appointments, setAppointments] = useState(initialAppointments);
  const [search, setSearch] = useState("");
  const [newAppointment, setNewAppointment] = useState({
    patientName: "",
    doctorName: "",
    date: "",
    time: "",
    purpose: "",
    status: "Scheduled",
    room: ""
  });

  // Filter appointments by patient name
  const filtered = appointments.filter(a =>
    a.patientName.toLowerCase().includes(search.toLowerCase())
  );

  // Admin functions
  const handleAdd = () => {
    if (!newAppointment.patientName || !newAppointment.doctorName) return;
    setAppointments([
      ...appointments,
      { id: appointments.length + 1, ...newAppointment }
    ]);
    setNewAppointment({
      patientName: "",
      doctorName: "",
      date: "",
      time: "",
      purpose: "",
      status: "Scheduled",
      room: ""
    });
  };

  const handleDelete = id => {
    setAppointments(appointments.filter(a => a.id !== id));
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>Appointments</h2>

      {/* Search bar */}
      <input
        type="text"
        placeholder="Search by patient name..."
        value={search}
        onChange={e => setSearch(e.target.value)}
        style={{ padding: "8px", width: "300px", marginBottom: "10px" }}
      />

      {/* Appointments table */}
      <table style={{ width: "100%", borderCollapse: "collapse", marginTop: "10px" }}>
        <thead>
          <tr>
            <th style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>ID</th>
            <th style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>Patient</th>
            <th style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>Doctor</th>
            <th style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>Date</th>
            <th style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>Time</th>
            <th style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>Purpose</th>
            <th style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>Status</th>
            <th style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>Room</th>
            {currentUser.role === "admin" && <th style={{ padding: "8px" }}>Actions</th>}
          </tr>
        </thead>
        <tbody>
          {filtered.map(a => (
            <tr key={a.id}>
              <td style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>{a.id}</td>
              <td style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>{a.patientName}</td>
              <td style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>{a.doctorName}</td>
              <td style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>{a.date}</td>
              <td style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>{a.time}</td>
              <td style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>{a.purpose}</td>
              <td style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>{a.status}</td>
              <td style={{ borderBottom: "1px solid #ddd", padding: "8px" }}>{a.room}</td>
              {currentUser.role === "admin" && (
                <td style={{ padding: "8px" }}>
                  <button onClick={() => handleDelete(a.id)}>Delete</button>
                </td>
              )}
            </tr>
          ))}
        </tbody>
      </table>

      {/* Admin Add New Appointment */}
      {currentUser.role === "admin" && (
        <div style={{ marginTop: "20px" }}>
          <h3>Add New Appointment</h3>
          <input
            type="text"
            placeholder="Patient Name"
            value={newAppointment.patientName}
            onChange={e => setNewAppointment({ ...newAppointment, patientName: e.target.value })}
            style={{ padding: "8px", marginRight: "5px" }}
          />
          <input
            type="text"
            placeholder="Doctor Name"
            value={newAppointment.doctorName}
            onChange={e => setNewAppointment({ ...newAppointment, doctorName: e.target.value })}
            style={{ padding: "8px", marginRight: "5px" }}
          />
          <input
            type="date"
            value={newAppointment.date}
            onChange={e => setNewAppointment({ ...newAppointment, date: e.target.value })}
            style={{ padding: "8px", marginRight: "5px" }}
          />
          <input
            type="time"
            value={newAppointment.time}
            onChange={e => setNewAppointment({ ...newAppointment, time: e.target.value })}
            style={{ padding: "8px", marginRight: "5px" }}
          />
          <input
            type="text"
            placeholder="Purpose"
            value={newAppointment.purpose}
            onChange={e => setNewAppointment({ ...newAppointment, purpose: e.target.value })}
            style={{ padding: "8px", marginRight: "5px" }}
          />
          <input
            type="text"
            placeholder="Room"
            value={newAppointment.room}
            onChange={e => setNewAppointment({ ...newAppointment, room: e.target.value })}
            style={{ padding: "8px", marginRight: "5px" }}
          />
          <button onClick={handleAdd} style={{ padding: "8px" }}>Add Appointment</button>
        </div>
      )}
    </div>
  );
}



