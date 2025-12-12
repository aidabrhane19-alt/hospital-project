from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patients.views import (
    PatientViewSet,
    DoctorViewSet,
    AppointmentViewSet,
    CustomAuthToken,
    patient_list,
    add_patient,
    edit_patient,
    delete_patient
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('admin/', admin.site.urls),

    # ==========================
    # HTML pages (frontend views)
    # ==========================
    path('', patient_list, name='patient_list'),
    path('add/', add_patient, name='add_patient'),
    path('edit/<int:pk>/', edit_patient, name='edit_patient'),
    path('delete/<int:pk>/', delete_patient, name='delete_patient'),
    path('patients/', include('patients.urls')),
    
    path('api/', include(router.urls)),
    path('api/login/', CustomAuthToken.as_view(), name='api_login'),
]
