from django.shortcuts import render
from assign_work_employee.models import AssignWorkEmployee
from assign_work_manager.models import AssignWorkManager
from employee_reg.models import EmployeeReg
import datetime


from vcrypt.models import Vcmsg
from django.core.files.storage import FileSystemStorage
import mimetypes
from qrcode import *
from stegano import lsb
from cv2 import cv2
from django.http import HttpResponse
from PIL import Image, ImageDraw
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from io import BytesIO
from crypqrshare import settings

# Create your views here.
def postassignwork(request,idd):
    obk=""
    ss=request.session["u_id"]
    obb=AssignWorkManager.objects.get(assign_id=idd)
    obb1=EmployeeReg.objects.filter(status='accepted')

    if request.method == 'POST':
        obj =AssignWorkEmployee()
        obj.assign_id = idd
        obj.manager_id= ss
        obj.emp_id = request.POST.get('emp')
        obj.work_status = 'pending'
        obj.description = request.POST.get('description')
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.save()
        obk='ll'
    context = {
            'w': obb,
            'y': obb1,
            'msg':obk
        }

    import smtplib
    try:
        ob = AssignWorkEmployee.objects.get(assign_emp_id=obj.emp_id)
        email = "projectmailbg@gmail.com"
        sub = "Assign work"
        msg = "Hi," + ob.emp.firstname + " ,assigned work" + ob.description
        text = f'subject : {sub} \n\n{msg}'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, 'iqjjrhsyerovorav')
        server.sendmail(email, str(ob.emp.username), text)
    except:
        pass

        # fileid = str(obj.assign_emp_id)
        #
        # pas = idd
        #
        # imgqr = make(pas)
        # qrpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + str(obj.assign_emp_id) + ".bmp"
        # imgqr.save(qrpath)
        # img = cv2.imread(qrpath)
        # det = cv2.QRCodeDetector()
        # val, pts, st_code = det.detectAndDecode(img)
        #
        # print("Qr value : " + val)
        #
        # # print(imgqr.)
        # # print(imgqr.box_size)
        # img = Image.new('RGB', (100, 30), color=(255, 255, 255))
        # # In[4]:
        #
        # d = ImageDraw.Draw(img)
        # d.text((12, 14), pas, fill=(0, 0, 0))
        #
        # gray = img.convert('L')
        # bw = gray.point(lambda x: 0 if x < 128 else 255, '1')
        #
        # img1 = Image.new('RGB', (200, 30), color=(255, 255, 255))
        # img2 = Image.new('RGB', (200, 30), color=(255, 255, 255))
        #
        # width, height = img.size
        #
        # for row in range(height):
        #     colind = 0
        #     for col in range(width):
        #         r, g, b = img.getpixel((col, row))
        #         if r == 255:
        #             img1.putpixel((colind, row), (255, 255, 255))
        #             img2.putpixel((colind, row), (255, 255, 255))
        #             colind += 1
        #             img1.putpixel((colind, row), (0, 0, 0))
        #             img2.putpixel((colind, row), (0, 0, 0))
        #             colind += 1
        #         else:
        #             img1.putpixel((colind, row), (0, 0, 0))
        #             img2.putpixel((colind, row), (255, 255, 255))
        #             colind += 1
        #             img1.putpixel((colind, row), (255, 255, 255))
        #             img2.putpixel((colind, row), (0, 0, 0))
        #             colind += 1
        #
        # imgname = fileid + "1.bmp"
        # imgname1 = fileid + "2.bmp"
        # imgname3 = fileid + "3.bmp"
        # imgname4 = fileid + "4.bmp"
        #
        # imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname
        #
        # imgpath3 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname3
        #
        # imgpath1 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname1
        #
        # imgpath4 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname4
        #
        # img1.save(imgpath)
        # img2.save(imgpath1)
        #
        # # imgpath
        #
        # secret = lsb.hide(imgpath1, str(obj.assign_emp_id))
        # secret.save(imgpath3)
        #
        # secret1 = lsb.hide(imgpath, pas)
        # secret1.save(imgpath4)
        #
        # context = {
        #     'fl': imgname3,
        # }
        #
        # return render(request, 'assign_work_employee/post_assign_work_employee.html',context)
    return render(request, 'assign_work_employee/post_assign_work_employee.html',context)


def assignwork(request):
    ss=request.session["u_id"]
    obj = AssignWorkEmployee.objects.filter(manager_id=ss)
    context = {
        'a': obj
    }


    return render(request, 'assign_work_employee/assign_work_employee.html',context)


def viewassignwork(request):
    ss=request.session["u_id"]
    obj = AssignWorkEmployee.objects.filter(emp_id=ss)
    context = {
        'b': obj
    }

    return render(request, 'assign_work_employee/view_assigned_work_employee.html', context)


def comp(request):
    obj = AssignWorkEmployee.objects.all()
    context = {
        'b': obj
    }

    return render(request, 'assign_work_employee/view_wrk_company.html', context)

def sts_upd(request,idd):
    if request.method == 'POST':
        obj = AssignWorkEmployee.objects.get(assign_emp_id=idd)
        obj.work_status = request.POST.get('work_status')
        obj.save()
        return viewassignwork(request)
    return render(request, 'assign_work_employee/update.html')



