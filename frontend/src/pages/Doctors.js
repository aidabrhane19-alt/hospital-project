
import React, { useState, useContext } from "react";

// Dummy data for doctors and appointments
const doctorsData = [
  { id: 1, name: "Dr. John Smith", specialization: "Cardiology" },
  { id: 2, name: "Dr. Alice Lee", specialization: "Neurology" },
];

const appointmentsData = [
  { doctorId: 1, patientName: "Michael Brown", time: "2025-12-13 10:00" },
  { doctorId: 1, patientName: "Sarah Connor", time: "2025-12-13 11:30" },
  { doctorId: 2, patientName: "Tom Hanks", time: "2025-12-13 09:00" },
];

// Mock context for logged-in user
const UserContext = React.createContext({ user: { id: 1, role: "doctor" } });

export default function Doctors() {
  const { user } = useContext(UserContext);
  const [searchTerm, setSearchTerm] = useState("");

  // Safety checks
  if (!user || user.role !== "doctor") {
    return <p style={{ padding: "20px", color: "red" }}>Access denied. Must be a doctor.</p>;
  }

  const doctorInfo = doctorsData.find((d) => d.id === user.id);

  if (!doctorInfo) {
    return <p style={{ padding: "20px", color: "red" }}>Doctor info not found.</p>;
  }

  // Filter appointments for this doctor and search term
  const filteredAppointments = appointmentsData.filter(
    (appt) =>
      appt.doctorId === doctorInfo.id &&
      appt.patientName.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>Welcome, {doctorInfo.name}</h2>
      <p>Specialization: {doctorInfo.specialization}</p>

      <div style={{ margin: "20px 0" }}>
        <input
          type="text"
          placeholder="Search by patient name..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          style={{ padding: "8px", width: "300px", fontSize: "14px" }}
        />
      </div>

      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th style={{ border: "1px solid #ddd", padding: "8px" }}>#</th>
            <th style={{ border: "1px solid #ddd", padding: "8px" }}>Doctor</th>
            <th style={{ border: "1px solid #ddd", padding: "8px" }}>Specialization</th>
            <th style={{ border: "1px solid #ddd", padding: "8px" }}>Patient</th>
            <th style={{ border: "1px solid #ddd", padding: "8px" }}>Appointment Time</th>
          </tr>
        </thead>
        <tbody>
          {filteredAppointments.length === 0 ? (
            <tr>
              <td colSpan="5" style={{ padding: "10px", textAlign: "center" }}>
                No appointments found.
              </td>
            </tr>
          ) : (
            filteredAppointments.map((appt, index) => (
              <tr key={index}>
                <td style={{ border: "1px solid #ddd", padding: "8px" }}>{index + 1}</td>
                <td style={{ border: "1px solid #ddd", padding: "8px" }}>{doctorInfo.name}</td>
                <td style={{ border: "1px solid #ddd", padding: "8px" }}>{doctorInfo.specialization}</td>
                <td style={{ border: "1px solid #ddd", padding: "8px" }}>{appt.patientName}</td>
                <td style={{ border: "1px solid #ddd", padding: "8px" }}>{appt.time}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}





