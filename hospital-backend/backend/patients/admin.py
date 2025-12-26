from django.contrib import admin
from .models import (
    CustomUser, Patient, Doctor, Appointment,
    Receptionist, Pharmacist, Nurse, Technician,
    Medication, Prescription, PrescriptionItem
)

# --------------------------
# CustomUser Admin
# --------------------------
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

# --------------------------
# Patient Admin
# --------------------------
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'contact_info', 'assigned_doctor')
    list_filter = ('gender',)
    search_fields = ('name', 'contact_info', 'address')

# --------------------------
# Doctor Admin
# --------------------------
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'availability', 'contact_info', 'phone', 'user')
    search_fields = ('name', 'specialization', 'contact_info')

# --------------------------
# Appointment Admin
# --------------------------
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'reason', 'status')
    list_filter = ('date', 'doctor', 'status')
    search_fields = ('patient__name', 'doctor__name', 'reason')

# --------------------------
# Staff Admin (Receptionist, Pharmacist, Nurse, Technician)
# --------------------------
@admin.register(Receptionist)
class ReceptionistAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'user')
    search_fields = ('name', 'contact_info')

@admin.register(Pharmacist)
class PharmacistAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'user')
    search_fields = ('name', 'contact_info')

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'user')
    search_fields = ('name', 'contact_info')

@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'user')
    search_fields = ('name', 'contact_info')

# --------------------------
# Medication Admin
# --------------------------
@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'stock')
    search_fields = ('name',)

# --------------------------
# Prescription & PrescriptionItem Admin
# --------------------------
@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'appointment', 'date', 'status')
    list_filter = ('status', 'date', 'doctor')
    search_fields = ('patient__name', 'doctor__name', 'notes')

@admin.register(PrescriptionItem)
class PrescriptionItemAdmin(admin.ModelAdmin):
    list_display = ('prescription', 'medication', 'dosage', 'quantity')
    search_fields = ('medication__name', 'dosage')
