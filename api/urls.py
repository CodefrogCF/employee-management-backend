from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.getEmployeeList, name='get_employee_list'),
    path('employees/add/', views.addEmployee, name='add_employee'),
    path('employees/add/<int:pk>/', views.updateEmployee, name='update_employee'),
    path('employees/delete/<int:pk>/', views.deleteEmployee, name='delete_employee'),
    path('departments/', views.getDepartmentList, name='get_department_list'),
    path('departments/add/', views.addDepartment, name='add_department'),
    path('departments/<int:pk>/', views.updateDepartment, name='update_department'),
    path('departments/<int:pk>/', views.deleteDepartment, name='delete_department'),
]