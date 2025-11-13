from django.shortcuts import render
from employee_reg.models import EmployeeReg

# Create your views here.
from login.models import Login


def employeereg(request):
    # ss=request.session["u_id"]
    if request.method == 'POST':
        uname=request.POST.get('uname')
        if Login.objects.filter(username=uname).exists():
            message="Username already exist"
        else:
            obj = EmployeeReg()
            obj.firstname = request.POST.get('fname')
            obj.lastname = request.POST.get('lname')
            obj.password = request.POST.get('pwd')
            obj.date_of_birth = request.POST.get('dob')
            obj.email = request.POST.get('email')
            obj.gender = request.POST.get('gndr')
            obj.address = request.POST.get('addr')
            obj.city = request.POST.get('city')
            obj.district = request.POST.get('dis')
            obj.pincode = request.POST.get('pin')
            obj.phone_number = request.POST.get('phn')
            obj.marital_status = request.POST.get('ms')
            obj.join_date = request.POST.get('jd')
            obj.type = request.POST.get('sp')
            obj.username=request.POST.get('uname')
            obj.manager_id =1
            obj.status = 'pending'
            obj.save()

            message="Registerd"
        context={
            'msg':message
        }
        return render(request, 'employee_reg/employee_reg.html',context)
    return render(request, 'employee_reg/employee_reg.html')


def manageemployee(request):
    obj = EmployeeReg.objects.filter(status='pending')
    context = {
        'b': obj
    }
    return render(request, 'employee_reg/manage_employee.html', context)


def viewemployee(request):
    obj = EmployeeReg.objects.filter(status='accepted')
    context = {
        'a': obj
    }
    return render(request, 'employee_reg/view_employee.html', context)


def accept(request, idd):
    obj = EmployeeReg.objects.get(emp_id=idd)
    obj.status = 'accepted'
    obj.save()
    ob = Login()
    ob.username = obj.username
    ob.password = obj.password
    ob.type = 'employee'
    ob.u_id = obj.emp_id
    ob.save()
    return manageemployee(request)

def reject(request, idd):
    ob = EmployeeReg.objects.get(emp_id=idd)
    ob.status = 'rejected'
    ob.save()
    return manageemployee(request)





