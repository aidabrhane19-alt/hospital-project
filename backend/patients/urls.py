from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .views import (
    patient_list, add_patient, edit_patient, delete_patient,
    doctor_list, add_doctor, edit_doctor, delete_doctor,
    appointment_list, add_appointment, edit_appointment, delete_appointment,
    staff_list, add_staff,
    pharmacy_dashboard, medication_list, add_medication,
    create_prescription, add_prescription_item, mark_dispensed,
    prescription_list,
    admin_dashboard, doctor_dashboard, receptionist_dashboard, pharmacist_dashboard,
    redirect_based_on_role,
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
    # Login / Logout
    path('login/', auth_views.LoginView.as_view(template_name='patients/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('api/login/', CustomAuthToken.as_view(), name='api_login'),

    # Redirect based on role
    path('redirect/', redirect_based_on_role, name='redirect_based_on_role'),

    # Dashboards
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/doctor/', doctor_dashboard, name='doctor_dashboard'),
    path('dashboard/receptionist/', receptionist_dashboard, name='receptionist_dashboard'),
    path('dashboard/pharmacist/', pharmacist_dashboard, name='pharmacist_dashboard'),

    # --------------------------
    # Patient Management
    # --------------------------
    path('', patient_list, name='patient_list'),
    path('patients/add/', add_patient, name='add_patient'),
    path('patients/<int:pk>/edit/', edit_patient, name='edit_patient'),
    path('patients/<int:pk>/delete/', delete_patient, name='delete_patient'),

    # --------------------------
    # Doctor Management
    # --------------------------
    path('doctors/', doctor_list, name='doctor_list'),
    path('doctors/add/', add_doctor, name='add_doctor'),
    path('doctors/<int:pk>/edit/', edit_doctor, name='edit_doctor'),
    path('doctors/<int:pk>/delete/', delete_doctor, name='delete_doctor'),

    # --------------------------
    # Staff Management
    # --------------------------
    path('staff/<str:staff_type>/', staff_list, name='staff_list'),
    path('staff/<str:staff_type>/add/', add_staff, name='add_staff'),

    # --------------------------
    # Appointment Management
    # --------------------------
    path('appointments/', appointment_list, name='appointment_list'),
    path('appointments/add/', add_appointment, name='add_appointment'),
    path('appointments/<int:pk>/edit/', edit_appointment, name='edit_appointment'),
    path('appointments/<int:pk>/delete/', delete_appointment, name='delete_appointment'),

    # --------------------------
    # Pharmacy / Prescription
    # --------------------------
    path('pharmacy/', pharmacy_dashboard, name='pharmacy_dashboard'),
    path('pharmacy/medications/', medication_list, name='medication_list'),
    path('pharmacy/medications/add/', add_medication, name='add_medication'),
    path('pharmacy/prescriptions/', prescription_list, name='prescription_list'),
    path('pharmacy/prescriptions/<int:patient_id>/create/', create_prescription, name='create_prescription'),
    path('pharmacy/prescriptions/<int:pk>/items/', add_prescription_item, name='add_prescription_item'),
    path('pharmacy/prescriptions/<int:prescription_id>/dispense/', mark_dispensed, name='mark_dispensed'),

    # --------------------------
    # API Routes
    # --------------------------
    path('api/', include(router.urls)),
]

