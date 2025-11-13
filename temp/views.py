from django.shortcuts import render
# Create your views here.
def home(request):

    return render(request, 'temp/home.html')

def company(request):

    return render(request, 'temp/company.html')

def manager(request):

    return render(request, 'temp/manager.html')

def employee(request):

    return render(request, 'temp/employee.html')




