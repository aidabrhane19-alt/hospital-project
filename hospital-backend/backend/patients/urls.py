from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import (
    public_home, about, contact, role_based_login, redirect_based_on_role,
    patient_list, add_patient, edit_patient, delete_patient,
    doctor_list, add_doctor, edit_doctor, delete_doctor,
    staff_list, add_staff, edit_staff, delete_staff,
    appointment_list, add_appointment, edit_appointment, delete_appointment,
    pharmacy_dashboard, medication_list, add_medication,
    create_prescription, add_prescription_item, mark_dispensed,
    prescription_list, user_list, add_user, edit_user, delete_user,
    admin_dashboard, doctor_dashboard, receptionist_dashboard, pharmacist_dashboard,
    PatientViewSet, DoctorViewSet, AppointmentViewSet,
    CustomAuthToken
)

# --------------------------
# API Routers
# --------------------------
router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)

# --------------------------
# URL Patterns
# --------------------------
urlpatterns = [
    # Public Pages
    path('', public_home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

    # Auth
    path('login/', role_based_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # User Management
    path('users/', user_list, name='user_list'),
    path('users/add/', add_user, name='add_user'),
    path('users/edit/<int:id>/', edit_user, name='edit_user'),
    path('users/delete/<int:id>/', delete_user, name='delete_user'),

    # Dashboards
    path('redirect/', redirect_based_on_role, name='redirect_based_on_role'),
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/doctor/', doctor_dashboard, name='doctor_dashboard'),
    path('dashboard/receptionist/', receptionist_dashboard, name='receptionist_dashboard'),
    path('dashboard/pharmacist/', pharmacist_dashboard, name='pharmacist_dashboard'),

    # Patients
    path('patients/', patient_list, name='patient_list'),
    path('patients/add/', add_patient, name='add_patient'),
    path('patients/<int:pk>/edit/', edit_patient, name='edit_patient'),
    path('patients/<int:pk>/delete/', delete_patient, name='delete_patient'),

    # Doctors
    path('doctors/', doctor_list, name='doctor_list'),
    path('our-doctors/', TemplateView.as_view(template_name='public/doctors.html'), name='our_doctors'),
    path('doctors/add/', add_doctor, name='add_doctor'),
    path('doctors/<int:pk>/edit/', edit_doctor, name='edit_doctor'),
    path('doctors/<int:pk>/delete/', delete_doctor, name='delete_doctor'),

    # Staff
    path('staff/<str:staff_type>/', staff_list, name='staff_list'),
    path('staff/<str:staff_type>/add/', add_staff, name='add_staff'),
    path('staff/<str:staff_type>/edit/<int:pk>/', edit_staff, name='edit_staff'),
    path('staff/<str:staff_type>/delete/<int:pk>/', delete_staff, name='delete_staff'),

    # Appointments
    path('appointments/', appointment_list, name='appointment_list'),
    path('appointments/add/', add_appointment, name='add_appointment'),
    path('appointments/<int:pk>/edit/', edit_appointment, name='edit_appointment'),
    path('appointments/<int:pk>/delete/', delete_appointment, name='delete_appointment'),

    # Pharmacy / Prescriptions
    path('pharmacy/', pharmacy_dashboard, name='pharmacy_dashboard'),
    path('pharmacy/medications/', medication_list, name='medication_list'),
    path('pharmacy/medications/add/', add_medication, name='add_medication'),
    path('pharmacy/prescriptions/', prescription_list, name='prescription_list'),
    path('pharmacy/prescriptions/<int:patient_id>/create/', create_prescription, name='create_prescription'),
    path('pharmacy/prescriptions/<int:pk>/items/', add_prescription_item, name='add_prescription_item'),
    path('pharmacy/prescriptions/<int:prescription_id>/dispense/', mark_dispensed, name='mark_dispensed'),

    # API
    path('api/', include(router.urls)),

    # Token Auth API
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]
