import React from "react";

function StaffList({ staff }) {
  // Ensure staff is always an array
  const staffArray = staff || [];

  const filteredStaff = staffArray.filter((member) => member.role !== "admin");

  return (
    <div style={{ padding: "20px" }}>
      <h2>Staff List</h2>
      {filteredStaff.length === 0 ? (
        <p>No staff found.</p>
      ) : (
        <ul>
          {filteredStaff.map((member, index) => (
            <li key={index}>
              {member.name} - {member.role}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

// Example usage with dummy data if no prop is passed
StaffList.defaultProps = {
  staff: [
    { name: "Alice", role: "nurse" },
    { name: "Bob", role: "technician" },
    { name: "Carol", role: "receptionist" },
  ],
};

export default StaffList;
