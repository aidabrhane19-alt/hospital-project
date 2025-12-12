from django.contrib import admin
from .models import CustomUser, Patient, Doctor, Appointment,  Receptionist, Pharmacist

# CustomUser admin
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

# Patient admin
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'contact_info', 'assigned_doctor')
    search_fields = ('name', 'contact_info')
    list_filter = ('gender',)

# Doctor admin
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'availability', 'contact_info', 'user')
    search_fields = ('name', 'specialization', 'contact_info')

# Appointment admin
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'purpose')
    list_filter = ('date', 'doctor')
    search_fields = ('patient__name', 'doctor__name', 'purpose')

# Receptionist admin
@admin.register(Receptionist)
class ReceptionistAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'user')
    search_fields = ('name', 'contact_info')

@admin.register(Pharmacist)
class PharmacistAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'user')
    search_fields = ('name', 'contact_info')