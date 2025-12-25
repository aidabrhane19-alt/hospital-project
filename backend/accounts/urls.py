from django.urls import path
from .views import (
    dashboard_redirect,
    staff_list,
    add_staff,
    edit_staff,
    delete_staff
)

urlpatterns = [
    path('dashboard/', dashboard_redirect, name='dashboard'),
    path('staff/', staff_list, name='staff_list'),
    path('staff/add/', add_staff, name='add_staff'),
    path('staff/edit/<int:user_id>/', edit_staff, name='edit_staff'),
    path('staff/delete/<int:user_id>/', delete_staff, name='delete_staff'),
]
