from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from patients.models import Doctor

@receiver(post_save, sender=User)
def create_doctor_profile(sender, instance, created, **kwargs):
    if created and instance.groups.filter(name='doctor').exists():
        Doctor.objects.create(user=instance)
