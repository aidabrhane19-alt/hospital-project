import React from "react";
import { Navigate } from "react-router-dom";

function ProtectedRoute({ allowedRoles, children, currentUser }) {
  if (!currentUser) return <Navigate to="/login" />;

  if (allowedRoles && !allowedRoles.includes(currentUser.role)) {
    return <h2 style={{ padding: "20px" }}>Access Denied</h2>;
  }

  return children;
}

export default ProtectedRoute;
