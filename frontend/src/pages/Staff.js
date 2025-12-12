// src/pages/Staff.js
import React, { useState } from "react";

const Staff = () => {
  const role = localStorage.getItem("role"); // "admin", "doctor", "staff", "patient"
  const isAdmin = role === "admin";

  const [staffList, setStaffList] = useState([]);
  const [newStaff, setNewStaff] = useState({
    name: "",
    position: "",
    contact: "",
  });

  const handleChange = (e) => {
    setNewStaff({ ...newStaff, [e.target.name]: e.target.value });
  };

  const handleAdd = (e) => {
    e.preventDefault();
    if (newStaff.name.trim() === "") return;

    setStaffList([
      ...staffList,
      { ...newStaff, id: staffList.length + 1 }
    ]);

    setNewStaff({ name: "", position: "", contact: "" });
  };

  const handleDelete = (id) => {
    setStaffList(staffList.filter((s) => s.id !== id));
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Staff Management</h1>

      {/* Only Admin Can Add Staff */}
      {isAdmin && (
        <form
          onSubmit={handleAdd}
          style={{
            background: "#f2f2f2",
            padding: "15px",
            borderRadius: "6px",
            marginBottom: "25px"
          }}
        >
          <h2>Add New Staff</h2>

          <input
            type="text"
            name="name"
            placeholder="Full Name"
            value={newStaff.name}
            onChange={handleChange}
            style={{ display: "block", margin: "8px 0", padding: "8px", width: "300px" }}
          />

          <input
            type="text"
            name="position"
            placeholder="Position (e.g., Nurse)"
            value={newStaff.position}
            onChange={handleChange}
            style={{ display: "block", margin: "8px 0", padding: "8px", width: "300px" }}
          />

          <input
            type="text"
            name="contact"
            placeholder="Contact Info"
            value={newStaff.contact}
            onChange={handleChange}
            style={{ display: "block", margin: "8px 0", padding: "8px", width: "300px" }}
          />

          <button
            type="submit"
            style={{
              padding: "10px 20px",
              background: "green",
              color: "white",
              border: "none",
              cursor: "pointer",
              borderRadius: "4px"
            }}
          >
            Add Staff
          </button>
        </form>
      )}

      {/* Staff Table */}
      <h2>Staff List</h2>

      {staffList.length === 0 ? (
        <p>No staff added yet.</p>
      ) : (
        <table
          style={{
            width: "100%",
            borderCollapse: "collapse",
            marginTop: "10px"
          }}
        >
          <thead>
            <tr style={{ background: "#333", color: "white" }}>
              <th style={{ padding: "8px", border: "1px solid #ddd" }}>ID</th>
              <th style={{ padding: "8px", border: "1px solid #ddd" }}>Name</th>
              <th style={{ padding: "8px", border: "1px solid #ddd" }}>Position</th>
              <th style={{ padding: "8px", border: "1px solid #ddd" }}>Contact</th>
              {isAdmin && <th style={{ padding: "8px", border: "1px solid #ddd" }}>Actions</th>}
            </tr>
          </thead>
          <tbody>
            {staffList.map((s) => (
              <tr key={s.id}>
                <td style={{ padding: "8px", border: "1px solid #ddd" }}>{s.id}</td>
                <td style={{ padding: "8px", border: "1px solid #ddd" }}>{s.name}</td>
                <td style={{ padding: "8px", border: "1px solid #ddd" }}>{s.position}</td>
                <td style={{ padding: "8px", border: "1px solid #ddd" }}>{s.contact}</td>

                {isAdmin && (
                  <td style={{ padding: "8px", border: "1px solid #ddd" }}>
                    <button
                      onClick={() => handleDelete(s.id)}
                      style={{
                        padding: "6px 12px",
                        background: "red",
                        color: "white",
                        border: "none",
                        cursor: "pointer",
                        borderRadius: "4px"
                      }}
                    >
                      Delete
                    </button>
                  </td>
                )}

              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default Staff;

