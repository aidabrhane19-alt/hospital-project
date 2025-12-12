import React, { useState, useEffect } from "react";

function PharmacyForm({ onSubmit, editData }) {
  const [name, setName] = useState("");
  const [type, setType] = useState("");
  const [quantity, setQuantity] = useState("");
  const [expiry, setExpiry] = useState("");

  useEffect(() => {
    if (editData) {
      setName(editData.name);
      setType(editData.type);
      setQuantity(editData.quantity);
      setExpiry(editData.expiry);
    }
  }, [editData]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ name, type, quantity, expiry });
    setName(""); setType(""); setQuantity(""); setExpiry("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Name" value={name} onChange={e => setName(e.target.value)} required />
      <input type="text" placeholder="Type" value={type} onChange={e => setType(e.target.value)} required />
      <input type="number" placeholder="Quantity" value={quantity} onChange={e => setQuantity(e.target.value)} required />
      <input type="date" value={expiry} onChange={e => setExpiry(e.target.value)} required />
      <button type="submit">{editData ? "Update" : "Add"}</button>
    </form>
  );
}

export default PharmacyForm;
