from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'salary', 'department', 'date_of_joining']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee.department.field.related_model  # Assuming department is a ForeignKey in Employee
        fields = ['department_name', 'department_manager', 'department_location', 'department_budget', 'department_phone_number']