import React, { useState, useEffect } from "react";

function StaffForm({ onSave, editingStaff, onCancel }) {
  const [staff, setStaff] = useState({
    name: "",
    role: "",
    contact: "",
    responsibilities: ""
  });

  useEffect(() => {
    if (editingStaff) setStaff(editingStaff);
  }, [editingStaff]);

  const handleChange = (e) => {
    setStaff({ ...staff, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave(staff);
    setStaff({ name: "", role: "", contact: "", responsibilities: "" });
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", width: "350px", margin: "20px auto" }}>
      <input name="name" placeholder="Staff Name" value={staff.name} onChange={handleChange} required />
      <select name="role" value={staff.role} onChange={handleChange} required>
        <option value="">Select Role</option>
        <option value="nurse">Nurse</option>
        <option value="receptionist">Receptionist</option>
        <option value="technician">Technician</option>
        <option value="admin">Admin</option>
      </select>
      <input name="contact" placeholder="Contact" value={staff.contact} onChange={handleChange} required />
      <textarea name="responsibilities" placeholder="Responsibilities" value={staff.responsibilities} onChange={handleChange} />
      <button type="submit" style={{ marginTop: "10px" }}>{editingStaff ? "Update" : "Add"} Staff</button>
      {editingStaff && <button type="button" onClick={onCancel} style={{ marginTop: "5px" }}>Cancel</button>}
    </form>
  );
}

export default StaffForm;
