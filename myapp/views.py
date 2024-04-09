import csv
from django.http import HttpResponse
from .models import Employee
from django.shortcuts import render, redirect
from .forms import EmployeeForm

def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'

    employees = Employee.objects.all()

    writer = csv.writer(response, delimiter=';')
    writer.writerow(['Name', 'Salary', 'Start Date'])

    for employee in employees:
        writer.writerow([employee.name, employee.salary, employee.start_date])

    return response