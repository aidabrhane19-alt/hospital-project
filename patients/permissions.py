from rest_framework import permissions

class HospitalRolePermissions(permissions.BasePermission):
    """
    Custom permissions for Hospital Management System.
    
    Roles:
    - Admin: Full access
    - Doctor: Can view own patients and appointments, update appointments
    - Receptionist: Can create patients and appointments, view records
    - Nurse: Can update patient vitals, view patients
    - Pharmacist: Can view patient prescriptions (read-only)
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        role = getattr(request.user, 'userprofile', None)
        if not role:
            return False

        role = role.role

        if role == 'admin':
            return True  # Full access

        if role == 'doctor':
            # Doctor can view patients/appointments and update appointments
            return request.method in ['GET', 'PUT', 'PATCH']

        if role == 'receptionist':
            # Receptionist can create patients/appointments, view lists
            return request.method in ['GET', 'POST']

        if role == 'nurse':
            # Nurse can view patients and update vitals (PATCH)
            return request.method in ['GET', 'PATCH']

        if role == 'pharmacist':
            # Pharmacist read-only
            return request.method == 'GET'

        return False

    def has_object_permission(self, request, view, obj):
        """
        Object-level permissions:
        - Doctor can only update their own patients/appointments
        - Receptionist cannot delete
        - Nurse and pharmacist can only view
        """
        role = getattr(request.user, 'userprofile', None)
        if not role:
            return False

        role = role.role

        if role == 'admin':
            return True

        if role == 'doctor':
            # Doctor can update only their patients or appointments
            if hasattr(obj, 'doctor'):
                return obj.doctor == request.user
            return False

        if role == 'receptionist':
            # Receptionist cannot delete
            return request.method != 'DELETE'

        if role in ['nurse', 'pharmacist']:
            # Only read-only
            return request.method == 'GET'

        return False
