from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import (
    CustomUser, Patient, Doctor, Appointment,
    Receptionist, Pharmacist, Nurse, Technician,
    Medication, Prescription, PrescriptionItem
)
from .forms import (
    PatientForm, DoctorForm, AppointmentForm,
    MedicationForm, PrescriptionItemForm
)
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer
from .permissions import HospitalRolePermissions

# --------------------------
# Helper decorators
# --------------------------
def role_required(role):
    return user_passes_test(lambda u: u.role == role)

def multi_role_required(roles):
    return user_passes_test(lambda u: u.role in roles)

# --------------------------
# Patient Views
# --------------------------
@login_required
def patient_list(request):
    if request.user.role in ['admin', 'receptionist']:
        patients = Patient.objects.all()
    elif request.user.role == 'doctor':
        patients = Patient.objects.filter(assigned_doctor__user=request.user)
    else:
        patients = Patient.objects.none()
    return render(request, 'patients/patient_list.html', {'patients': patients})

@login_required
@multi_role_required(['admin', 'receptionist'])
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})

@login_required
@multi_role_required(['admin', 'receptionist'])
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/edit_patient.html', {'form': form, 'patient': patient})

@login_required
@role_required('admin')
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patients/delete_patient.html', {'patient': patient})

# --------------------------
# Doctor Views
# --------------------------
@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

@login_required
@role_required('admin')
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctors/add_doctor.html', {'form': form})

@login_required
@role_required('admin')
def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, id=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/edit_doctor.html', {'form': form, 'doctor': doctor})

@login_required
@role_required('admin')
def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, id=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctors/delete_doctor.html', {'doctor': doctor})

# --------------------------
# Staff Views (Receptionist, Pharmacist, Nurse, Technician)
# --------------------------
@login_required
@role_required('admin')
def staff_list(request, staff_type):
    staff_model = {
        'receptionist': Receptionist,
        'pharmacist': Pharmacist,
        'nurse': Nurse,
        'technician': Technician
    }.get(staff_type)
    if not staff_model:
        return redirect('admin_dashboard')
    staff_members = staff_model.objects.all()
    return render(request, 'staff/staff_list.html', {'staff_members': staff_members, 'staff_type': staff_type})

@login_required
@role_required('admin')
def add_staff(request, staff_type):
    staff_model = {
        'receptionist': Receptionist,
        'pharmacist': Pharmacist,
        'nurse': Nurse,
        'technician': Technician
    }.get(staff_type)
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_info = request.POST.get('contact_info')
        staff_model.objects.create(name=name, contact_info=contact_info)
        return redirect('staff_list', staff_type=staff_type)
    return render(request, 'staff/add_staff.html', {'staff_type': staff_type})

# --------------------------
# Appointment Views
# --------------------------
@login_required
def appointment_list(request):
    if request.user.role in ['admin', 'receptionist']:
        appointments = Appointment.objects.all().order_by('-date', '-time')
    elif request.user.role == 'doctor':
        appointments = Appointment.objects.filter(doctor__user=request.user)
    else:
        appointments = Appointment.objects.none()
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

@login_required
@multi_role_required(['admin', 'receptionist'])
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/add_appointment.html', {'form': form})

@login_required
@multi_role_required(['admin', 'receptionist'])
def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/edit_appointment.html', {'form': form, 'appointment': appointment})

@login_required
@role_required('admin')
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointments/delete_appointment.html', {'appointment': appointment})

# --------------------------
# Pharmacy & Prescription Views
# --------------------------
@login_required
@multi_role_required(['pharmacist', 'admin'])
def pharmacy_dashboard(request):
    prescriptions = Prescription.objects.all().order_by('-date')
    return render(request, 'pharmacy/dashboard.html', {'prescriptions': prescriptions})

@login_required
@multi_role_required(['pharmacist', 'admin'])
def medication_list(request):
    meds = Medication.objects.all()
    return render(request, 'pharmacy/medication_list.html', {'meds': meds})

@login_required
@multi_role_required(['pharmacist', 'admin'])
def add_medication(request):
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medication_list')
    else:
        form = MedicationForm()
    return render(request, 'pharmacy/add_medication.html', {'form': form})

@login_required
@role_required('doctor')
def create_prescription(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        notes = request.POST.get('notes')
        prescription = Prescription.objects.create(
            patient=patient,
            doctor=request.user.doctor_profile,
            notes=notes
        )
        medication_ids = request.POST.getlist('medication')
        dosages = request.POST.getlist('dosage')
        quantities = request.POST.getlist('quantity')
        durations = request.POST.getlist('duration')
        for i in range(len(medication_ids)):
            PrescriptionItem.objects.create(
                prescription=prescription,
                medication_id=medication_ids[i],
                dosage=dosages[i],
                quantity=quantities[i],
                duration=durations[i]
            )
        return redirect('prescription_list')
    medications = Medication.objects.all()
    return render(request, 'pharmacy/create_prescription.html', {'patient': patient, 'medications': medications})

@login_required
@multi_role_required(['pharmacist', 'admin'])
def add_prescription_item(request, pk):
    prescription = get_object_or_404(Prescription, id=pk)
    if request.method == 'POST':
        form = PrescriptionItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.prescription = prescription
            item.save()
            item.medication.stock -= item.quantity
            item.medication.save()
            return redirect('add_prescription_item', pk=pk)
    else:
        form = PrescriptionItemForm()
    items = PrescriptionItem.objects.filter(prescription=prescription)
    return render(request, 'pharmacy/add_prescription_item.html', {
        'form': form, 'prescription': prescription, 'items': items
    })

@login_required
@multi_role_required(['pharmacist', 'admin'])
def mark_dispensed(request, prescription_id):
    prescription = get_object_or_404(Prescription, id=prescription_id)
    prescription.status = 'dispensed'
    prescription.save()
    return redirect('pharmacy_dashboard')

@login_required
def prescription_list(request):
    if request.user.role == 'doctor':
        prescriptions = Prescription.objects.filter(doctor=request.user.doctor_profile)
    else:
        prescriptions = Prescription.objects.all()
    return render(request, 'pharmacy/prescription_list.html', {'prescriptions': prescriptions})

# --------------------------
# Dashboards
# --------------------------
@login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'dashboard/doctor_dashboard.html')

@login_required
def receptionist_dashboard(request):
    return render(request, 'dashboard/receptionist_dashboard.html')

@login_required
def pharmacist_dashboard(request):
    return render(request, 'dashboard/pharmacist_dashboard.html')

@login_required
def redirect_based_on_role(request):
    role = request.user.role
    return redirect({
        'admin': 'admin_dashboard',
        'doctor': 'doctor_dashboard',
        'receptionist': 'receptionist_dashboard',
        'pharmacist': 'pharmacist_dashboard'
    }.get(role, 'login'))

# --------------------------
# REST API Viewsets
# --------------------------
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated, HospitalRolePermissions]

    def get_queryset(self):
        user = self.request.user
        role = getattr(user, 'role', None)
        if role in ['admin', 'receptionist']:
            return Patient.objects.all()
        if role == 'doctor':
            return Patient.objects.filter(assigned_doctor__user=user)
        return Patient.objects.none()

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, HospitalRolePermissions]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated, HospitalRolePermissions]

    def get_queryset(self):
        user = self.request.user
        role = getattr(user, 'role', None)
        if role in ['admin', 'receptionist']:
            return Appointment.objects.all()
        if role == 'doctor':
            return Appointment.objects.filter(doctor__user=user)
        return Appointment.objects.none()

# --------------------------
# Custom Token Authentication
# --------------------------
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'username': user.username})
