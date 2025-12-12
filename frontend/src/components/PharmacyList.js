import React from "react";

function PharmacyList({ medicines, onEdit, onDelete }) {
  if (!medicines || medicines.length === 0) return <p>No medicines.</p>;
  return (
    <table border="1" style={{ width: "100%", marginTop: "10px" }}>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Quantity</th>
          <th>Expiry</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {medicines.map((med, index) => (
          <tr key={index} style={{ backgroundColor: med.quantity < 5 ? "#ffe6e6" : "white" }}>
            <td>{med.name}</td>
            <td>{med.type}</td>
            <td>{med.quantity}</td>
            <td>{med.expiry}</td>
            <td>
              <button onClick={() => onEdit(index)}>Edit</button>
              <button onClick={() => onDelete(index)}>Delete</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default PharmacyList;
