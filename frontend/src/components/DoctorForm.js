import React, { useState, useEffect } from "react";

function DoctorForm({ onSubmit, editData }) {
  const [name, setName] = useState("");
  const [specialization, setSpecialization] = useState("");
  const [availability, setAvailability] = useState("");
  const [contact, setContact] = useState("");

  // Load data into form when editing
  useEffect(() => {
    if (editData) {
      setName(editData.name);
      setSpecialization(editData.specialization);
      setAvailability(editData.availability);
      setContact(editData.contact);
    }
  }, [editData]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ name, specialization, availability, contact });
    // Clear form after submission
    setName("");
    setSpecialization("");
    setAvailability("");
    setContact("");
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
      <input
        type="text"
        placeholder="Doctor Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
        style={{ marginRight: "10px" }}
      />
      <input
        type="text"
        placeholder="Specialization"
        value={specialization}
        onChange={(e) => setSpecialization(e.target.value)}
        required
        style={{ marginRight: "10px" }}
      />
      <input
        type="text"
        placeholder="Availability (e.g., Mon-Fri 9am-5pm)"
        value={availability}
        onChange={(e) => setAvailability(e.target.value)}
        required
        style={{ marginRight: "10px" }}
      />
      <input
        type="text"
        placeholder="Contact Info"
        value={contact}
        onChange={(e) => setContact(e.target.value)}
        required
        style={{ marginRight: "10px" }}
      />
      <button type="submit">{editData ? "Update" : "Add"} Doctor</button>
    </form>
  );
}

export default DoctorForm;
