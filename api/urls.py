from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.getEmployeeList, name='get_employee_list'),
    path('employee/add/', views.addEmployee, name='add_employee'),
    path('employee/add/<int:pk>/', views.updateEmployee, name='update_employee'),
    path('employee/delete/<int:pk>/', views.deleteEmployee, name='delete_employee'),
    path('department/', views.getDepartmentList, name='get_department_list'),
    path('department/add/', views.addDepartment, name='add_department'),
    path('department/<int:pk>/', views.updateDepartment, name='update_department'),
    path('department/<int:pk>/', views.deleteDepartment, name='delete_department'),
]