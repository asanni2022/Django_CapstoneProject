from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import default_storage

from SalaryApp.models import Employee, Department
from SalaryApp.serializers import EmployeeSerializer, DepartmentSerializer

# Create Views here

@csrf_exempt
def employeeApi(request, id=0):
    try:
        if request.method == 'GET':
            employees = Employee.objects.all()
            employees_serializer = EmployeeSerializer(employees, many=True)
            return JsonResponse(employees_serializer.data, safe=False)

        elif request.method == 'POST':
            employee_data = JSONParser().parse(request)
            employee_serializer = EmployeeSerializer(data=employee_data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return JsonResponse("Added Successfully", safe=False)
            return JsonResponse(employee_serializer.errors, status=400)

        elif request.method == 'PUT':
            employee_data = JSONParser().parse(request)
            try:
                employee = Employee.objects.get(pk=id)
                employee_serializer = EmployeeSerializer(employee, data=employee_data)
                if employee_serializer.is_valid():
                    employee_serializer.save()
                    return JsonResponse("Updated Successfully", safe=False)
                return JsonResponse(employee_serializer.errors, status=400)
            except Employee.DoesNotExist:
                return JsonResponse("Employee not found", status=404)

        elif request.method == 'DELETE':
            try:
                employee = Employee.objects.get(pk=id)
                employee.delete()
                return JsonResponse("Deleted Successfully", safe=False)
            except Employee.DoesNotExist:
                return JsonResponse("Employee not found", status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def departmentApi(request, id=0):
    try:
        if request.method == 'GET':
            departments = Department.objects.all()
            departments_serializer = DepartmentSerializer(departments, many=True)
            return JsonResponse(departments_serializer.data, safe=False)

        elif request.method == 'POST':
            department_data = JSONParser().parse(request)
            department_serializer = DepartmentSerializer(data=department_data)
            if department_serializer.is_valid():
                department_serializer.save()
                return JsonResponse("Added Successfully", safe=False)
            return JsonResponse(department_serializer.errors, status=400)
        
        elif request.method == 'PUT':
            department_data = JSONParser().parse(request)
            try:
                department = Department.objects.get(pk=id)
                department_serializer = DepartmentSerializer(department, data=department_data)
                if department_serializer.is_valid():
                    department_serializer.save()
                    return JsonResponse("Updated Successfully", safe=False)
                return JsonResponse(department_serializer.errors, status=400)
            except Department.DoesNotExist:
                return JsonResponse("Department not found", status=404)

        elif request.method == 'DELETE':
            try:
                department = Department.objects.get(pk=id)
                department.delete()
                return JsonResponse("Deleted Successfully", safe=False)
            except Department.DoesNotExist:
                return JsonResponse("Department not found", status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def SaveFile(request):
    if request.method == 'POST':
        file = request.FILES.get('uploadedFile', None)
        if file:
            file_name = default_storage.save(file.name, file)
            return JsonResponse({'message': 'File uploaded successfully', 'file_name': file_name}, safe=False)
        else:
            return JsonResponse({'message': 'No File Provided'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

def home_salaryapp_view(request):
    return HttpResponse("Hello Employees! Welcome to the SalaryApp API. Let's Make Magic HaPpEn!!!")


