from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_first_name', 'employee_last_name', 'employee_date_of_birth', 'employee_email', 'employee_phone_number', 'employee_salary', 'employee_department', 'employee_position', 'employee_date_of_joining']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee.employee_department.field.related_model  # Assuming department is a ForeignKey in Employee
        fields = ['department_name', 'department_manager', 'department_budget', 'department_revenue']