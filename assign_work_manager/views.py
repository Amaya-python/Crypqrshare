from django.shortcuts import render
from assign_work_manager.models import AssignWorkManager
from manager_reg.models import ManagerReg
from work.models import Work
import datetime
# Create your views here.
def postassign(request,idd):
    obb=Work.objects.get(work_id=idd)
    obb1=ManagerReg.objects.all()
    context={
        'v':obb,
        'w':obb1
    }
    if request.method == 'POST':
        obj =AssignWorkManager()
        obj.manager_id = request.POST.get('man')
        obj.work_id = idd
        obj.work_details = request.POST.get('work_details')
        obj.work_status = 'pending'
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.save()

        import smtplib
        try:
            ob = AssignWorkManager.objects.get(assign_id=obj.manager_id)
            email = "projectmailbg@gmail.com"
            sub = "Assign work"
            msg = "Hi," + ob.manager.firstname + " ,assigned work" + ob.work_details
            text = f'subject : {sub} \n\n{msg}'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, 'iqjjrhsyerovorav')
            server.sendmail(email, str(ob.manager.username), text)
        except:
            pass
    return render(request, 'assign_work_manager/post_assign_work_manager.html', context)


def compassign(request):
    ss=request.session["u_id"]
    obj = AssignWorkManager.objects.filter(manager_id=ss)
    context = {
        'b': obj
    }
    return render(request, 'assign_work_manager/assign_work_manager.html', context)


def viewassign(request):
    ss=request.session["u_id"]
    obj = AssignWorkManager.objects.filter(manager_id=ss)
    context = {
        'a': obj
    }
    return render(request, 'assign_work_manager/view_assigned_work_manager.html', context)

def viewassmngr(request):
    obj = AssignWorkManager.objects.all()
    context = {
        'b': obj
    }

    return render(request, 'assign_work_manager/view_mangrwork.html', context)



