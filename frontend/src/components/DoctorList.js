import React, { useState, useEffect } from "react";
import axios from "axios";

const DoctorList = () => {
  const [doctors, setDoctors] = useState([]); // default empty array
  const [search, setSearch] = useState("");

  // Load doctors from API
  useEffect(() => {
    const fetchDoctors = async () => {
      try {
        const res = await axios.get("http://localhost:5000/doctors");
        setDoctors(res.data || []); // fallback if undefined
      } catch (err) {
        console.error("Error fetching doctors:", err);
        setDoctors([]); // fallback
      }
    };

    fetchDoctors();
  }, []);

  // Safe filter
  const filteredDoctors = doctors.filter((d) =>
    d.name?.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div style={{ padding: "20px" }}>
      <h2>Doctors</h2>

      <input
        type="text"
        placeholder="Search doctor..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        style={{
          padding: "8px",
          marginBottom: "20px",
          width: "250px",
          border: "1px solid #ccc",
        }}
      />

      <table border="1" cellPadding="10" style={{ borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th>Name</th>
            <th>Specialization</th>
            <th>Contact</th>
            <th>Availability</th>
          </tr>
        </thead>

        <tbody>
          {filteredDoctors.length > 0 ? (
            filteredDoctors.map((d) => (
              <tr key={d.id}>
                <td>{d.name}</td>
                <td>{d.specialization}</td>
                <td>{d.contact}</td>
                <td>{d.availability}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4">No doctors found.</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default DoctorList;
