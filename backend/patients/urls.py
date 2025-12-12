from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .views import (
    patient_list, add_patient, edit_patient, delete_patient,
    doctor_list, add_doctor, edit_doctor, delete_doctor,
    appointment_list, add_appointment, edit_appointment, delete_appointment,
    medication_list, add_medication, prescription_list, 
    add_prescription_item, pharmacy_dashboard, mark_dispensed,
    admin_dashboard, doctor_dashboard, receptionist_dashboard,
    pharmacist_dashboard, redirect_based_on_role,
    DoctorViewSet, AppointmentViewSet,
    CustomAuthToken
)

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    # Patient management
    path('', patient_list, name='patient_list'),
    path('add/', add_patient, name='add_patient'),
    path('edit/<int:pk>/', edit_patient, name='edit_patient'),
    path('delete/<int:pk>/', delete_patient, name='delete_patient'),

    # HTML Login / Logout
    path('login/', auth_views.LoginView.as_view(template_name='patients/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # API login
    path('api/login/', CustomAuthToken.as_view(), name='api_login'),

    # Dashboards
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/doctor/', doctor_dashboard, name='doctor_dashboard'),
    path('dashboard/receptionist/', receptionist_dashboard, name='receptionist_dashboard'),
    path('dashboard/pharmacist/', pharmacist_dashboard, name='pharmacist_dashboard'),
    path('redirect/', redirect_based_on_role, name='redirect_based_on_role'),

    # Doctors
    path('doctors/', doctor_list, name='doctor_list'),
    path('doctors/add/', add_doctor, name='add_doctor'),
    path('doctors/<int:pk>/edit/', edit_doctor, name='edit_doctor'),
    path('doctors/<int:pk>/delete/', delete_doctor, name='delete_doctor'),

    # Appointments
    path('appointments/', appointment_list, name='appointment_list'),
    path('appointments/add/', add_appointment, name='add_appointment'),
    path('appointments/<int:pk>/edit/', edit_appointment, name='edit_appointment'),
    path('appointments/<int:pk>/delete/', delete_appointment, name='delete_appointment'),

    # Pharmacy
    path('pharmacy/', pharmacy_dashboard, name='pharmacy_dashboard'),
    path('pharmacy/medications/', medication_list, name='medication_list'),
    path('pharmacy/medications/add/', add_medication, name='add_medication'),
    path('pharmacy/prescriptions/', prescription_list, name='prescription_list'),
    path('pharmacy/prescriptions/<int:pk>/items/', add_prescription_item, name='add_prescription_item'),
    path('pharmacy/dispense/<int:prescription_id>/', mark_dispensed, name='mark_dispensed'),

    # API router
    path('api/', include(router.urls)),
]
