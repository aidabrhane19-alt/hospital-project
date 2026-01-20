from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser, Patient, Doctor, Appointment,
    Receptionist, Pharmacist, Nurse, Technician,
    Medication, Prescription, PrescriptionItem
)

# --------------------------
# CustomUser Admin
# --------------------------
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'role', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
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
