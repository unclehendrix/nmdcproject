from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.index,name='dashboard-index'),
    path('staff/',views.staff, name='dashboard-staff'),
    path('staff/delete/<int:pk>/',views.staff_delete, name='dashboard-staff-delete'),
    path('staff/update/<int:pk>/',views.staff_update, name='dashboard-staff-update'),
    path('management/',views.management, name='dashboard-management'),
    path('department/',views.department, name='dashboard-department'),
    path('department/delete/<int:pk>/',views.department_delete, name='dashboard-department-delete'),
    path('department/update/<int:pk>/',views.department_update, name='dashboard-department-update'), 
    path('unit/',views.unit, name='dashboard-unit'),
    path('unit/delete/<int:pk>/',views.unit_delete, name='dashboard-unit-delete'),
    path('unit/update/<int:pk>/',views.unit_update, name='dashboard-unit-update'),
    path('division/',views.division, name='dashboard-division'),
    path('division/delete/<int:pk>/',views.division_delete, name='dashboard-division-delete'),
    path('division/update/<int:pk>/', views.division_update, name='dashboard-division-update'),
    path('generate_pdf/', views.generate_pdf, name='generate-pdf'),
]
