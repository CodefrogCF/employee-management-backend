from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeeSerializer, DepartmentSerializer
from .models import Employee, Department
from rest_framework import viewsets

# Create your views here.

###########################   Views for Employee Management API   ###########################

@api_view(['GET'])
def getEmployeeList(request):

#    Retrieve a list of all employees.

    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addEmployee(request):

#    Add a new employee.

    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def updateEmployee(request, pk):

#    Update an existing employee.

    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=404)

    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def deleteEmployee(request, pk):

#    Delete an existing employee.

    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=404)

    employee.delete()
    return Response({'message': 'Employee deleted successfully'}, status=200)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

###########################   ViewSet for Department Management API   ###########################

@api_view(['GET'])
def getDepartmentList(request):

#    Retrieve a list of all departments.

    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addDepartment(request):

#    Add a new department.

    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def updateDepartment(request, pk):

#    Update an existing department.

    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({'error': 'Department not found'}, status=404)

    serializer = DepartmentSerializer(department, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def deleteDepartment(request, pk):

#    Delete an existing department.

    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({'error': 'Department not found'}, status=404)

    department.delete()
    return Response({'message': 'Department deleted successfully'}, status=200)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer