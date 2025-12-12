import React, { useState } from "react";
import PharmacyList from "../components/PharmacyList";
import PharmacyForm from "../components/PharmacyForm";

function Pharmacy({ medicines, setMedicines, appointments, setAppointments, user }) {
  const [editIndex, setEditIndex] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");

  const handleAddOrUpdate = (med) => {
    const updated = [...medicines];
    if (editIndex !== null) {
      updated[editIndex] = med;
      setEditIndex(null);
    } else {
      updated.push(med);
    }
    setMedicines(updated);
    localStorage.setItem("medicines", JSON.stringify(updated));
  };

  const handleEdit = (index) => setEditIndex(index);
  const handleDelete = (index) => {
    if (window.confirm("Delete this medicine?")) {
      const updated = medicines.filter((_, i) => i !== index);
      setMedicines(updated);
      localStorage.setItem("medicines", JSON.stringify(updated));
    }
  };
  const markDispensed = (index) => {
    if (window.confirm("Mark as dispensed?")) {
      const updatedAppointments = [...appointments];
      updatedAppointments[index].medicationDispensed = true;
      updatedAppointments[index].dispensedBy = user.name;
      setAppointments(updatedAppointments);
      localStorage.setItem("appointments", JSON.stringify(updatedAppointments));
    }
  };

  const filteredMedicines = medicines.filter((med) =>
    med.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    med.type.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div style={{ maxWidth: "800px", margin: "20px auto" }}>
      <h2>Pharmacy</h2>
      <input type="text" placeholder="Search medicine" value={searchTerm} onChange={e => setSearchTerm(e.target.value)} />
      <PharmacyForm onSubmit={handleAddOrUpdate} editData={editIndex !== null ? medicines[editIndex] : null} />
      <PharmacyList medicines={filteredMedicines} onEdit={handleEdit} onDelete={handleDelete} />

      <h3>Appointments</h3>
      <ul>
        {appointments.map((a, i) => (
          <li key={i}>
            {a.patientName} - {a.purpose} - {a.date} {a.time}
            <button onClick={() => markDispensed(i)} disabled={a.medicationDispensed}>
              {a.medicationDispensed ? "Dispensed" : "Mark Dispensed"}
            </button>
            {a.medicationDispensed && <span> - Dispensed by: {a.dispensedBy}</span>}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Pharmacy;
