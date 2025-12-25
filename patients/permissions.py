from rest_framework import permissions

class HospitalRolePermissions(permissions.BasePermission):
    """
    Custom permissions for Hospital Management System.

    Roles:
    - Admin: Full access
    - Doctor: Can view and update their own patients and appointments
    - Receptionist: Can create and view patients and appointments, cannot delete
    - Nurse: Can view patients and update vitals (read-only for other actions)
    - Pharmacist: Can view prescriptions (read-only)
    """

    def has_permission(self, request, view):
        # Must be authenticated
        if not request.user or not request.user.is_authenticated:
            return False

        role = getattr(request.user, 'role', None)
        if not role:
            return False

        # Admin has full access
        if role == 'admin':
            return True

        # Doctor can view and update (GET, PUT, PATCH)
        if role == 'doctor':
            return request.method in ['GET', 'PUT', 'PATCH']

        # Receptionist can view and create (GET, POST)
        if role == 'receptionist':
            return request.method in ['GET', 'POST']

        # Nurse can view and partially update (GET, PATCH)
        if role == 'nurse':
            return request.method in ['GET', 'PATCH']

        # Pharmacist can only view (GET)
        if role == 'pharmacist':
            return request.method == 'GET'

        return False

    def has_object_permission(self, request, view, obj):
        # Must be authenticated
        if not request.user or not request.user.is_authenticated:
            return False

        role = getattr(request.user, 'role', None)
        if not role:
            return False

        # Admin can do anything
        if role == 'admin':
            return True

        # Doctor can access only their own patients or appointments
        if role == 'doctor':
            if hasattr(obj, 'doctor'):
                return obj.doctor.user == request.user
            return False

        # Receptionist cannot delete
        if role == 'receptionist':
            return request.method != 'DELETE'

        # Nurse and Pharmacist are read-only at object level
        if role in ['nurse', 'pharmacist']:
            return request.method == 'GET'

        return False
