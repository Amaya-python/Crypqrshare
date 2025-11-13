from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login
# Create your views here.
from employee_reg.models import EmployeeReg
def login(request):
    if request.method=="POST":
        name = request.POST.get("uname")
        password = request.POST.get("pwd")
        obj = Login.objects.filter(username=name,password=password)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "company":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/company/')
            elif tp =="manager":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/manager/')
            elif tp == "employee":
                uob=EmployeeReg.objects.get(emp_id=uid)
                if uob.status=='accepted':
                    request.session["u_id"]=uid
                    return HttpResponseRedirect('/temp/employee/')
                else:
                    objilist = "Your registraion is pending!"
                    context = {
                        'msg': objilist,
                    }
                    return render(request, 'login/login.html', context)
        else:
                objilist = "incorrect username or password......please try again.....!"
                context = {
                    'msg':objilist,
                }
                return render(request, 'login/login.html',context)
    return render(request,'login/login.html')


from manager_reg.models import ManagerReg
import smtplib
def forget_password(request):
    email="projectmailbg@gmail.com"
    if request.method=="POST":
        uname=request.POST.get('mail')
        if Login.objects.filter(username=uname).exists():
            ob=Login.objects.get(username=uname)
            pwd=ob.password
            if ob.type=="employee":
                uob=EmployeeReg.objects.get(emp_id=ob.u_id)
                em=uob.email
            elif ob.type=="manager":
                uob=ManagerReg.objects.get(manager_id=ob.u_id)
                em=uob.email
            else:
                em="amayasurendran148@gmail.com"
            sub="Forget password"
            msg="Username: "+uname+'& Password: '+pwd
            text=f'subject : {sub} \n\n{msg}'
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email,'iqjjrhsyerovorav')
            server.sendmail(email,str(em),text)
        else:
            message="Invalid username"
            context={
                'msg':message
            }
            return render(request, 'login/forget_pwd.html',context)
    return render(request, 'login/forget_pwd.html')


