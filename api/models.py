from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_first_name = models.CharField(max_length=100)
    employee_last_name = models.CharField(max_length=100)
    employee_date_of_birth = models.DateField()
    employee_email = models.EmailField(max_length=100)
    employee_phone_number = models.CharField(max_length=100)
    employee_department = models.ForeignKey('Department', on_delete=models.CASCADE)
    employee_position = models.CharField(max_length=100, default='Employee')
    employee_salary = models.IntegerField()
    employee_date_of_joining = models.DateField()


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_manager = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='managed_departments', null=True, blank=True)
    department_budget = models.IntegerField()
    department_revenue = models.IntegerField(default=0)
    department_employees = models.ManyToManyField(Employee, related_name='departments', blank=True)