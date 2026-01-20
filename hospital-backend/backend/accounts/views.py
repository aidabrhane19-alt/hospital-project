from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

@login_required
def dashboard_redirect(request):
    """
    Redirect users to the correct dashboard based on their role.
    """
    role = request.user.userprofile.role

    if role == 'admin':
        return render(request, 'dashboard/admin_dashboard.html')
    elif role == 'doctor':
        return render(request, 'dashboard/doctor_dashboard.html')
    elif role == 'receptionist':
        return render(request, 'dashboard/receptionist_dashboard.html')
    elif role == 'pharmacist':
        return render(request, 'dashboard/pharmacist_dashboard.html')
    elif role == 'nurse':
        return render(request, 'dashboard/nurse_dashboard.html')
    else:
        return redirect('logout')

@login_required
def staff_list(request):
    staff = UserProfile.objects.exclude(role='doctor').exclude(role='admin')
    return render(request, 'accounts/staff_list.html', {'staff': staff})


@login_required
def add_staff(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        role = request.POST.get('role')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if form.is_valid():
            user = form.save()
            profile = user.userprofile
            profile.role = role
            profile.phone = phone
            profile.address = address
            profile.save()
            return redirect('staff_list')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/add_staff.html', {'form': form})


@login_required
def edit_staff(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = user.userprofile

    if request.method == 'POST':
        profile.role = request.POST.get('role')
        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')
        profile.save()
        return redirect('staff_list')

    return render(request, 'accounts/edit_staff.html', {
        'user': user,
        'profile': profile
    })


@login_required
def delete_staff(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('staff_list')

    return render(request, 'accounts/delete_staff.html', {'user': user})
