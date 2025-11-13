from django.shortcuts import render
from manager_reg.models import ManagerReg
from login.models import Login
# Create your views here.
def managerreg(request):
    if request.method == 'POST':
        uname=request.POST.get('uname')
        if Login.objects.filter(username=uname).exists():
            message="Username already exist"
        else:
            obj = ManagerReg()
            obj.firstname = request.POST.get('fname')
            obj.lastname = request.POST.get('lname')
            obj.password = request.POST.get('pwd')  #
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
            obj.username=request.POST.get('uname')
            obj.save()

            ob=Login()
            ob.username=obj.username
            ob.password=obj.password
            ob.type='manager'
            ob.u_id=obj.manager_id
            ob.save()
            message = "Registerd"
        context = {
            'msg': message
        }
        return render(request, 'manager_reg/manager_reg.html',context)
    return render(request, 'manager_reg/manager_reg.html')


def updatemanagerprofile(request):
    ss=request.session["u_id"]
    obj = ManagerReg.objects.filter(manager_id=ss)
    context = {
        'b': obj
    }
    return render(request, 'manager_reg/update_manager_profile.html', context)
def profileviewmanager(request,idd) :
    obj = ManagerReg.objects.get(manager_id=idd)
    context = {
        'c': obj
    }
    if request.method == 'POST':
        obj = ManagerReg.objects.get(manager_id=idd)
        obj.firstname = request.POST.get('fname')
        obj.lastname = request.POST.get('lname')
        obj.password = request.POST.get('pwd')
        obj.date_of_birth = request.POST.get('date')
        obj.email = request.POST.get('email')
        obj.gender = request.POST.get('gndr')
        obj.address = request.POST.get('addr')
        obj.city = request.POST.get('city')
        obj.district = request.POST.get('dis')
        obj.pincode = request.POST.get('pin')
        obj.phone_number = request.POST.get('phn')
        obj.marital_status = request.POST.get('ms')
        obj.join_date = request.POST.get('jd')

        obj.save()
        return updatemanagerprofile(request)

    return render(request, 'manager_reg/profile_view_manager.html', context)


def viewmanager(request):
    obj = ManagerReg.objects.all()
    context = {
        'a': obj
    }
    return render(request, 'manager_reg/view_manager.html',context)

def delete(request, idd):
    ob = ManagerReg.objects.get(manager_id=idd)
    ob.delete()
    return updatemanagerprofile(request)





def comp(request):
    obj = ManagerReg.objects.all()
    context = {
        'a': obj
    }
    return render(request, 'manager_reg/view_admin.html',context)



