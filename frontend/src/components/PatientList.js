import React from "react";

const patients = [
  { id: 1, name: "John Doe", age: 22, disease: "Flu" },
  { id: 2, name: "Sarah Smith", age: 30, disease: "Malaria" }
];

export default function PatientList() {

  // Prevent crash if patients is missing
  if (!patients || !Array.isArray(patients)) {
    return <p>Loading patients...</p>;
  }

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Patient List</h2>

      {patients.length === 0 ? (
        <p>No patients found.</p>
      ) : (
        <table className="w-full border">
          <thead>
            <tr className="bg-gray-200">
              <th className="p-2 border">ID</th>
              <th className="p-2 border">Name</th>
              <th className="p-2 border">Age</th>
              <th className="p-2 border">Disease</th>
            </tr>
          </thead>
          <tbody>
            {patients.map((p) => (
              <tr key={p.id}>
                <td className="border p-2">{p.id}</td>
                <td className="border p-2">{p.name}</td>
                <td className="border p-2">{p.age}</td>
                <td className="border p-2">{p.disease}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
