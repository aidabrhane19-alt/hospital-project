from rest_framework import serializers
from .models import (
    Patient, Doctor, Appointment,
    Receptionist, Pharmacist, Nurse, Technician,
    Medication, Prescription, PrescriptionItem
)

# --------------------------
# Patient Serializer
# --------------------------
class PatientSerializer(serializers.ModelSerializer):
    assigned_doctor_name = serializers.CharField(source='assigned_doctor.name', read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'

# --------------------------
# Doctor Serializer
# --------------------------
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'user', 'name', 'specialization', 'availability', 'contact_info', 'phone']

# --------------------------
# Appointment Serializer
# --------------------------
class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'

# --------------------------
# Staff Serializers
# --------------------------
class ReceptionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptionist
        fields = ['id', 'name', 'contact_info', 'user']

class PharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist
        fields = ['id', 'name', 'contact_info', 'user']

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ['id', 'name', 'contact_info', 'user']

class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = ['id', 'name', 'contact_info', 'user']

# --------------------------
# Medication Serializer
# --------------------------
class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id', 'name', 'description', 'stock']

# --------------------------
# Prescription Serializer
# --------------------------
class PrescriptionItemSerializer(serializers.ModelSerializer):
    medication_name = serializers.CharField(source='medication.name', read_only=True)

    class Meta:
        model = PrescriptionItem
        fields = ['id', 'prescription', 'medication', 'medication_name', 'dosage', 'quantity', 'duration']

class PrescriptionSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    items = PrescriptionItemSerializer(source='prescriptionitem_set', many=True, read_only=True)

    class Meta:
        model = Prescription
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_name', 'appointment', 'date', 'notes', 'status', 'items']
