import React, { useState } from "react";
import AppointmentForm from "./AppointmentForm";

function AppointmentList({ patients, doctors, appointments, setAppointments }) {
  const [editingAppointment, setEditingAppointment] = useState(null);
  const [search, setSearch] = useState("");

  const handleSave = (appointment) => {
    if (editingAppointment) {
      setAppointments(appointments.map(a => a === editingAppointment ? appointment : a));
      setEditingAppointment(null);
    } else {
      setAppointments([...appointments, appointment]);
    }
  };

  const handleDelete = (appointment) => {
    if (window.confirm("Are you sure you want to cancel this appointment?")) {
      setAppointments(appointments.filter(a => a !== appointment));
    }
  };

  const filteredAppointments = appointments.filter(a =>
    a.patientName.toLowerCase().includes(search.toLowerCase()) ||
    a.doctorName.toLowerCase().includes(search.toLowerCase())
  );

  const getPatientHistory = (name) => {
    const patient = patients.find(p => p.name === name);
    return patient ? patient.medicalHistory : [];
  };

  return (
    <div style={{ textAlign: "center" }}>
      <h2>Appointments</h2>
      <input
        placeholder="Search by patient or doctor"
        value={search}
        onChange={e => setSearch(e.target.value)}
        style={{ marginBottom: "10px", padding: "5px", width: "250px" }}
      />

      <AppointmentForm
        onSave={handleSave}
        editingAppointment={editingAppointment}
        onCancel={() => setEditingAppointment(null)}
        patients={patients}
        doctors={doctors}
      />

      <ul style={{ listStyle: "none", padding: 0 }}>
        {filteredAppointments.map((a, i) => (
          <li key={i} style={{ margin: "10px 0", border: "1px solid #ccc", padding: "10px" }}>
            <strong>{a.patientName}</strong> (Medical History: {getPatientHistory(a.patientName).join(", ") || "None"})
            with <strong>{a.doctorName}</strong> <br />
            {a.date} at {a.time} | Purpose: {a.purpose} <br />
            <button onClick={() => setEditingAppointment(a)} style={{ marginRight: "5px" }}>Edit</button>
            <button onClick={() => handleDelete(a)}>Cancel</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AppointmentList;
