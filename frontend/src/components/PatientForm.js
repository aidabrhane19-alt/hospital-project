import React, { useState, useEffect } from "react";

function PatientForm({ onSave, editingPatient, onCancel }) {
  const [patient, setPatient] = useState({
    name: "",
    age: "",
    gender: "",
    contact: "",
    address: "",
    medicalHistory: ""
  });

  useEffect(() => {
    if (editingPatient) {
      // Convert medicalHistory array to comma-separated string for form
      setPatient({
        ...editingPatient,
        medicalHistory: editingPatient.medicalHistory ? editingPatient.medicalHistory.join(", ") : ""
      });
    }
  }, [editingPatient]);

  const handleChange = (e) => {
    setPatient({ ...patient, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Split medical history into array
    const newPatient = { 
      ...patient, 
      medicalHistory: patient.medicalHistory
        ? patient.medicalHistory.split(",").map(m => m.trim())
        : [] 
    };
    onSave(newPatient);
    setPatient({ name: "", age: "", gender: "", contact: "", address: "", medicalHistory: "" });
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", width: "300px", margin: "20px auto" }}>
      <input name="name" placeholder="Name" value={patient.name} onChange={handleChange} required />
      <input name="age" placeholder="Age" value={patient.age} onChange={handleChange} required />
      <select name="gender" value={patient.gender} onChange={handleChange} required>
        <option value="">Gender</option>
        <option value="Male">Male</option>
        <option value="Female">Female</option>
      </select>
      <input name="contact" placeholder="Contact" value={patient.contact} onChange={handleChange} required />
      <input name="address" placeholder="Address" value={patient.address} onChange={handleChange} required />
      <textarea 
        name="medicalHistory" 
        placeholder="Medical History (comma separated)" 
        value={patient.medicalHistory} 
        onChange={handleChange} 
      />
      <p style={{ fontSize: "12px", color: "gray" }}>Separate multiple records with commas.</p>
      <button type="submit" style={{ marginTop: "10px" }}>{editingPatient ? "Update" : "Add"} Patient</button>
      {editingPatient && <button type="button" onClick={onCancel} style={{ marginTop: "5px" }}>Cancel</button>}
    </form>
  );
}

export default PatientForm;
