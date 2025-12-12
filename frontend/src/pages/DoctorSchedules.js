import React from "react";

function DoctorSchedules() {
  // Temporary dummy user for testing
  const user = { role: "admin" };

  if (!user) {
    return <p>Loading...</p>; // fallback if user is undefined
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>Doctor Schedules</h2>

      {user.role === "doctor" ? (
        <p>Welcome, doctor! Here are your schedules:</p>
      ) : (
        <p>You do not have permission to view this page.</p>
      )}

      {/* Example schedule list */}
      <ul>
        <li>Dr. John - 10:00 AM - 12:00 PM</li>
        <li>Dr. Mary - 01:00 PM - 03:00 PM</li>
        <li>Dr. Smith - 03:30 PM - 05:00 PM</li>
      </ul>
    </div>
  );
}

export default DoctorSchedules;
