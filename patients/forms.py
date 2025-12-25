from django import forms
from .models import (
    Patient, Doctor, Appointment,
    Medication, Prescription, PrescriptionItem,
    Receptionist, Pharmacist, Nurse, Technician
)

# --------------------------
# Patient Form
# --------------------------
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'contact_info', 'address', 'medical_history', 'assigned_doctor']

# --------------------------
# Doctor Form
# --------------------------
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'availability', 'contact_info', 'phone']

# --------------------------
# Appointment Form
# --------------------------
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'time', 'purpose', 'status']

# --------------------------
# Medication Form
# --------------------------
class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'description', 'stock']

# --------------------------
# Prescription Form
# --------------------------
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'doctor', 'appointment', 'notes', 'status']

# --------------------------
# Prescription Item Form
# --------------------------
class PrescriptionItemForm(forms.ModelForm):
    class Meta:
        model = PrescriptionItem
        fields = ['medication', 'dosage', 'quantity', 'duration']

# --------------------------
# Staff Forms
# --------------------------
class ReceptionistForm(forms.ModelForm):
    class Meta:
        model = Receptionist
        fields = ['name', 'contact_info', 'user']

class PharmacistForm(forms.ModelForm):
    class Meta:
        model = Pharmacist
        fields = ['name', 'contact_info', 'user']

class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ['name', 'contact_info', 'user']

class TechnicianForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = ['name', 'contact_info', 'user']
