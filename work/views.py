from django.shortcuts import render
from work.models import Work
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

def addwork(request):
        if request.method == 'POST':
            obj = Work()
            obj.file = request.POST.get('work')
            obj.work_status = 'pending'
            obj.date = datetime.datetime.today()
            obj.save()

            fileid = str(obj.work_id)

            pas = request.POST.get('work')

            imgqr = make(pas)
            qrpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + str(obj.work_id) + ".bmp"
            imgqr.save(qrpath)

            img = cv2.imread(qrpath)
            det = cv2.QRCodeDetector()
            val, pts, st_code = det.detectAndDecode(img)

            print("Qr value : " + val)

            # print(imgqr.)
            # print(imgqr.box_size)
            img = Image.new('RGB', (100, 30), color=(255, 255, 255))
            # In[4]:

            d = ImageDraw.Draw(img)
            d.text((12, 14), pas, fill=(0, 0, 0))

            gray = img.convert('L')
            bw = gray.point(lambda x: 0 if x < 128 else 255, '1')

            img1 = Image.new('RGB', (200, 30), color=(255, 255, 255))
            img2 = Image.new('RGB', (200, 30), color=(255, 255, 255))

            width, height = img.size

            for row in range(height):
                colind = 0
                for col in range(width):
                    r, g, b = img.getpixel((col, row))
                    if r == 255:
                        img1.putpixel((colind, row), (255, 255, 255))
                        img2.putpixel((colind, row), (255, 255, 255))
                        colind += 1
                        img1.putpixel((colind, row), (0, 0, 0))
                        img2.putpixel((colind, row), (0, 0, 0))
                        colind += 1
                    else:
                        img1.putpixel((colind, row), (0, 0, 0))
                        img2.putpixel((colind, row), (255, 255, 255))
                        colind += 1
                        img1.putpixel((colind, row), (255, 255, 255))
                        img2.putpixel((colind, row), (0, 0, 0))
                        colind += 1

            imgname = fileid + "1.bmp"
            imgname1 = fileid + "2.bmp"
            imgname3 = fileid + "3.bmp"
            imgname4 = fileid + "4.bmp"

            imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname

            imgpath3 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname3

            imgpath1 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname1

            imgpath4 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname4

            img1.save(imgpath)
            img2.save(imgpath1)

            # imgpath

            secret = lsb.hide(imgpath1, str(obj.work_id))
            secret.save(imgpath3)

            secret1 = lsb.hide(imgpath, pas)
            secret1.save(imgpath4)

            context = {
                'fl': imgname3,
            }
            return render(request, 'work/add_work.html', context)
        return render(request, 'work/add_work.html')


def updateworkstatus(request,idd):
    if request.method == 'POST':
        obj = Work.objects.get(work_id=idd)
        obj.work_status = request.POST.get('work_status')
        obj.save()
        return viewworkstatus(request)
    return render(request, 'work/update_work_status.html')



def viewworkstatus(request):
    obj = Work.objects.all()
    context = {
        'a': obj
    }
    return render(request, 'work/view_workstatus.html', context)

def viewworkstatusmanager(request):
    obj = Work.objects.all()
    context = {
        'b': obj
    }
    return render(request, 'work/view_workstatus_manager.html', context)


