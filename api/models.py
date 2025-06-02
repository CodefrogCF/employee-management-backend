from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    date_of_joining = models.DateField()

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_manager = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='managed_departments', null=True, blank=True)
    department_location = models.CharField(max_length=100)
    department_budget = models.IntegerField()
    department_phone_number = models.CharField(max_length=100)