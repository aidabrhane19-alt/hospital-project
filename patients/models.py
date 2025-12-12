from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('receptionist', 'Receptionist'),
        ('pharmacist', 'Pharmacist'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='receptionist')

    def __str__(self):
        return f"{self.username} ({self.role})"

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,related_name='doctor_profile')
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.specialization})"
    
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_info = models.CharField(max_length=100)
    address = models.TextField()
    medical_history = models.TextField(blank=True, null=True)
    assigned_doctor = models.ForeignKey("Doctor", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='pending'
    )

    def __str__(self):
        return f"{self.patient.name} with {self.doctor.name} on {self.date}"


class Receptionist(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    medications = models.ManyToManyField('Medication', through='PrescriptionItem')

    notes = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('dispensed', 'Dispensed')],
        default='pending'
    )    
    def __str__(self):
        return f"Prescription for {self.patient.name} by {self.doctor.name}"

class PrescriptionItem(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medication = models.ForeignKey('Medication', on_delete=models.CASCADE)
    dosage = models.CharField(max_length=255)
    quantity = models.IntegerField(max_length=50)

    def __str__(self):
        return f"{self.medication.name} ({self.dosage})"

class Pharmacist(models.Model):
        name = models.CharField(max_length=100)
        contact_info = models.CharField(max_length=50)
        user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

        def __str__(self):
           return self.name
        
class Medication(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name









@receiver(post_save, sender=CustomUser)
def create_doctor_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'doctor':
        # Check if a Doctor with the same name exists
        doctor, created_doctor = Doctor.objects.get_or_create(name=instance.username)
        doctor.user = instance
        doctor.save()
    elif instance.role == 'receptionist':
            receptionist, _ = Receptionist.objects.get_or_create(name=instance.username)
            receptionist.user = instance
            receptionist.save()    