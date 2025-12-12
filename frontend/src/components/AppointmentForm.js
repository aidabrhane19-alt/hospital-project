import React, { useState, useEffect } from "react";

function AppointmentForm({ onSave, editingAppointment, patients, doctors, onCancel }) {
  const [appointment, setAppointment] = useState({
    patientName: "",
    doctorName: "",
    date: "",
    time: "",
    purpose: ""
  });

  useEffect(() => {
    if (editingAppointment) setAppointment(editingAppointment);
  }, [editingAppointment]);

  const handleChange = (e) => {
    setAppointment({ ...appointment, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!appointment.patientName || !appointment.doctorName) {
      alert("Please select a patient and a doctor");
      return;
    }
    onSave(appointment);
    setAppointment({ patientName: "", doctorName: "", date: "", time: "", purpose: "" });
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", width: "350px", margin: "20px auto" }}>
      <select name="patientName" value={appointment.patientName} onChange={handleChange} required>
        <option value="">Select Patient</option>
        {patients.map((p, i) => <option key={i} value={p.name}>{p.name}</option>)}
      </select>

      <select name="doctorName" value={appointment.doctorName} onChange={handleChange} required>
        <option value="">Select Doctor</option>
        {doctors.map((d, i) => <option key={i} value={d.name}>{d.name}</option>)}
      </select>

      <input type="date" name="date" value={appointment.date} onChange={handleChange} required />
      <input type="time" name="time" value={appointment.time} onChange={handleChange} required />
      <input type="text" name="purpose" placeholder="Purpose" value={appointment.purpose} onChange={handleChange} />

      <button type="submit" style={{ marginTop: "10px" }}>{editingAppointment ? "Update" : "Schedule"} Appointment</button>
      {editingAppointment && <button type="button" onClick={onCancel} style={{ marginTop: "5px" }}>Cancel</button>}
    </form>
  );
}

export default AppointmentForm;
