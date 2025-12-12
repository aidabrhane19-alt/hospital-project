// src/pages/Patients.js
import React, { useState } from "react";

const Patients = () => {
  const [patients, setPatients] = useState([]);
  const [search, setSearch] = useState("");
  const [newPatient, setNewPatient] = useState({
    name: "",
    age: "",
    gender: "",
    contact: "",
    address: "",
    medicalHistory: ""
  });
  const [editId, setEditId] = useState(null);

  const handleChange = (e) => {
    setNewPatient({ ...newPatient, [e.target.name]: e.target.value });
  };

  const handleAddOrUpdatePatient = (e) => {
    e.preventDefault();
    if (!newPatient.name) return;

    if (editId !== null) {
      // Update existing patient
      setPatients(patients.map(p => p.id === editId ? { ...newPatient, id: editId } : p));
      setEditId(null);
    } else {
      // Add new patient
      setPatients([...patients, { ...newPatient, id: patients.length + 1 }]);
    }

    setNewPatient({ name: "", age: "", gender: "", contact: "", address: "", medicalHistory: "" });
  };

  const handleEdit = (id) => {
    const patient = patients.find(p => p.id === id);
    setNewPatient({ ...patient });
    setEditId(id);
  };

  const handleDelete = (id) => {
    setPatients(patients.filter(p => p.id !== id));
  };

  const filteredPatients = patients.filter(p =>
    p.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1 style={{ color: "#2c3e50" }}>Patients Management</h1>

      {/* Search */}
      <input
        type="text"
        placeholder="Search by name..."
        value={search}
        onChange={e => setSearch(e.target.value)}
        style={{ padding: "8px", marginBottom: "20px", width: "300px" }}
      />

      {/* Add / Edit Patient Form */}
      <form onSubmit={handleAddOrUpdatePatient} style={{ marginBottom: "30px", background: "#ecf0f1", padding: "20px", borderRadius: "8px" }}>
        <h2 style={{ color: "#2980b9" }}>{editId !== null ? "Edit Patient" : "Add New Patient"}</h2>
        <input placeholder="Name" name="name" value={newPatient.name} onChange={handleChange} style={{ display:"block", margin:"10px 0", padding:"8px", width:"300px" }} />
        <input placeholder="Age" name="age" type="number" value={newPatient.age} onChange={handleChange} style={{ display:"block", margin:"10px 0", padding:"8px", width:"300px" }} />
        <input placeholder="Gender" name="gender" value={newPatient.gender} onChange={handleChange} style={{ display:"block", margin:"10px 0", padding:"8px", width:"300px" }} />
        <input placeholder="Contact Info" name="contact" value={newPatient.contact} onChange={handleChange} style={{ display:"block", margin:"10px 0", padding:"8px", width:"300px" }} />
        <input placeholder="Address" name="address" value={newPatient.address} onChange={handleChange} style={{ display:"block", margin:"10px 0", padding:"8px", width:"300px" }} />
        <textarea placeholder="Medical History" name="medicalHistory" value={newPatient.medicalHistory} onChange={handleChange} style={{ display:"block", margin:"10px 0", padding:"8px", width:"300px" }} />
        <button type="submit" style={{ padding: "10px 20px", background: "#27ae60", color: "white", border: "none", borderRadius: "5px", cursor: "pointer" }}>
          {editId !== null ? "Update Patient" : "Add Patient"}
        </button>
      </form>

      {/* Patients Table */}
      <div style={{ overflowX: "auto" }}>
        <h2 style={{ color: "#2980b9" }}>Patients List</h2>
        {filteredPatients.length === 0 ? (
          <p>No patients found.</p>
        ) : (
          <table style={{ borderCollapse: "collapse", width: "100%" }}>
            <thead>
              <tr style={{ background: "#34495e", color: "white" }}>
                <th style={{ border: "1px solid #ddd", padding: "8px" }}>ID</th>
                <th style={{ border: "1px solid #ddd", padding: "8px" }}>Name</th>
                <th style={{ border: "1px solid #ddd", padding: "8px" }}>Age</th>
                <th style={{ border: "1px solid #ddd", padding: "8px" }}>Gender</th>
                <th style={{ border: "1px solid #ddd", padding: "8px" }}>Contact</th>
                <th style={{ border: "1px solid #ddd", padding: "8px" }}>Address</th>
                <th style={{ border: "1px solid #ddd", padding: "8px" }}>Medical History</th>
                <th style={{ border: "1px solid #ddd", padding: "8px" }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {filteredPatients.map((p) => (
                <tr key={p.id} style={{ borderBottom: "1px solid #ddd" }}>
                  <td style={{ padding: "8px" }}>{p.id}</td>
                  <td style={{ padding: "8px" }}>{p.name}</td>
                  <td style={{ padding: "8px" }}>{p.age}</td>
                  <td style={{ padding: "8px" }}>{p.gender}</td>
                  <td style={{ padding: "8px" }}>{p.contact}</td>
                  <td style={{ padding: "8px" }}>{p.address}</td>
                  <td style={{ padding: "8px" }}>{p.medicalHistory}</td>
                  <td style={{ padding: "8px" }}>
                    <button onClick={() => handleEdit(p.id)} style={{ marginRight: "5px" }}>Edit</button>
                    <button onClick={() => handleDelete(p.id)}>Delete</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
};

export default Patients;







