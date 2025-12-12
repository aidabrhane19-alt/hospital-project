import Sidebar from "../components/Sidebar";
import ProtectedRoute from "../components/ProtectedRoute";

function Profile({ currentUser }) {
  return (
    <ProtectedRoute allowedRoles={["admin","doctor","receptionist","nurse","technician"]}>
      <div style={{ display: "flex", flexWrap: "wrap" }}>
        <Sidebar currentUser={currentUser} />
        <div style={{ marginLeft: window.innerWidth > 768 ? "220px" : "0", padding: "20px", width: "100%" }}>
          <h2>User Profile</h2>
          {currentUser ? (
            <div style={{ maxWidth: "400px" }}>
              <p><strong>Name:</strong> {currentUser.name}</p>
              <p><strong>Role:</strong> {currentUser.role}</p>
              {currentUser.doctorId !== undefined && <p><strong>Doctor ID:</strong> {currentUser.doctorId}</p>}
            </div>
          ) : <p>No user information available.</p>}
        </div>
      </div>
    </ProtectedRoute>
  );
}

export default Profile;
