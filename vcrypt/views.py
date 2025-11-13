from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image, ImageDraw
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from io import BytesIO
from crypqrshare import settings
# Create your views here.
from vcrypt.models import Vcmsg
from django.core.files.storage import FileSystemStorage
import mimetypes
from qrcode import *
from stegano import lsb
from cv2 import cv2


def encpass(request):
    if request.method=="POST":

        ob=Vcmsg()
        ob.save()

        fileid=str(ob.id)

        pas=request.POST.get('msg')

        imgqr = make(pas)
        qrpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + str(ob.id) + ".bmp"
        imgqr.save(qrpath)


        img = cv2.imread(qrpath)
        det = cv2.QRCodeDetector()
        val, pts, st_code = det.detectAndDecode(img)

        print("Qr value : "+val)

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


        imgname=fileid+"1.bmp"
        imgname1=fileid+"2.bmp"
        imgname3 = fileid + "3.bmp"
        imgname4 = fileid + "4.bmp"


        imgpath=str(settings.BASE_DIR)+ str(settings.STATIC_URL)+imgname

        imgpath3 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname3

        imgpath1 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname1

        imgpath4 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname4

        img1.save(imgpath)
        img2.save(imgpath1)

        # imgpath

        secret = lsb.hide(imgpath1, str(ob.id))
        secret.save(imgpath3)

        secret1 = lsb.hide(imgpath, pas)
        secret1.save(imgpath4)

        context={
            'fl': imgname3,
        }
        return render(request,'vcrypt/message.html',context)
    return render(request,'vcrypt/message.html')


def dec_file(request):
    # img = Image.new('RGB', (100, 30), color=(255, 255, 255))
    # pas="Hello"
    # # In[49]:
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

    fileid="7"
    # img1 = Image.new('RGB', (200, 30), color=(255, 255, 255))
    # img2 = Image.new('RGB', (200, 30), color=(255, 255, 255))
    #
    # imgname = fileid + "1.bmp"
    # imgname1 = fileid + "2.bmp"
    #
    # imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname
    # imgpath1 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname1
    #
    # # imgname = "nm.bmp"
    #
    # imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname
    #
    #
    # img1 = Image.open(imgpath)
    #
    #
    #
    # width1, height1 = img1.size
    # imgout = Image.new('RGB', (100, 30), color=(255, 255, 255))
    # for row in range(height1):
    #     colind = 0
    #     for col in range(0, width1, 2):
    #         r, g, b = img1.getpixel((col, row))
    #         r1, g1, b1 = img2.getpixel((col, row))
    #         if (r == 255 and r1 == 255):
    #             imgout.putpixel((colind, row), (255, 255, 255))
    #         else:
    #             imgout.putpixel((colind, row), (0, 0, 0))
    #         colind += 1
    #
    # imgname = "merge.bmp"
    #
    # imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname
    # imgout.save(imgpath)
    # imgout.close()

    if request.method=="POST":
        mfile = request.FILES['file']
        fs = FileSystemStorage()
        fname = fs.save(mfile.name, mfile)

        print(fname)


        fileid = "7"
        # imgname3 = fileid + "3.bmp"
        imgpath3 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + fname
        fileid = lsb.reveal(imgpath3)
        print('id')
        # print(secret_text)

        imgname4 = fileid + "4.bmp"
        imgpath4 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname4
        secret_text = lsb.reveal(imgpath4)

        print("message")


        return HttpResponse(secret_text)
    return render(request,'vcrypt/decrypt.html')


def employee(request):
    # img = Image.new('RGB', (100, 30), color=(255, 255, 255))
    # pas="Hello"
    # # In[49]:
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

    fileid="7"
    # img1 = Image.new('RGB', (200, 30), color=(255, 255, 255))
    # img2 = Image.new('RGB', (200, 30), color=(255, 255, 255))
    #
    # imgname = fileid + "1.bmp"
    # imgname1 = fileid + "2.bmp"
    #
    # imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname
    # imgpath1 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname1
    #
    # # imgname = "nm.bmp"
    #
    # imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname
    #
    #
    # img1 = Image.open(imgpath)
    #
    #
    #
    # width1, height1 = img1.size
    # imgout = Image.new('RGB', (100, 30), color=(255, 255, 255))
    # for row in range(height1):
    #     colind = 0
    #     for col in range(0, width1, 2):
    #         r, g, b = img1.getpixel((col, row))
    #         r1, g1, b1 = img2.getpixel((col, row))
    #         if (r == 255 and r1 == 255):
    #             imgout.putpixel((colind, row), (255, 255, 255))
    #         else:
    #             imgout.putpixel((colind, row), (0, 0, 0))
    #         colind += 1
    #
    # imgname = "merge.bmp"
    #
    # imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname
    # imgout.save(imgpath)
    # imgout.close()

    if request.method=="POST":
        mfile = request.FILES['file']
        fs = FileSystemStorage()
        fname = fs.save(mfile.name, mfile)

        print(fname)


        fileid = "7"
        # imgname3 = fileid + "3.bmp"
        imgpath3 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + fname
        fileid = lsb.reveal(imgpath3)
        print('id')
        # print(secret_text)

        imgname4 = fileid + "4.bmp"
        imgpath4 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname4
        secret_text = lsb.reveal(imgpath4)

        print("message")


        return HttpResponse(secret_text)
    return render(request,'vcrypt/manager_decryption.html')



def manager(request):
    if request.method=="POST":

        ob=Vcmsg()
        ob.save()

        fileid=str(ob.id)

        pas=request.POST.get('msg')

        imgqr = make(pas)
        qrpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + str(ob.id) + ".bmp"
        imgqr.save(qrpath)


        img = cv2.imread(qrpath)
        det = cv2.QRCodeDetector()
        val, pts, st_code = det.detectAndDecode(img)

        print("Qr value : "+val)

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


        imgname=fileid+"1.bmp"
        imgname1=fileid+"2.bmp"
        imgname3 = fileid + "3.bmp"
        imgname4 = fileid + "4.bmp"


        imgpath=str(settings.BASE_DIR)+ str(settings.STATIC_URL)+imgname

        imgpath3 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname3

        imgpath1 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname1

        imgpath4 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + imgname4

        img1.save(imgpath)
        img2.save(imgpath1)

        # imgpath

        secret = lsb.hide(imgpath1, str(ob.id))
        secret.save(imgpath3)

        secret1 = lsb.hide(imgpath, pas)
        secret1.save(imgpath4)

        context={
            'fl': imgname3,
        }
        return render(request,'vcrypt/manager_msg.html',context)



        # secret_text = lsb.reveal(imgpath3)
        # print("message")
        # print(secret_text)
        # secret_text = lsb.reveal(imgpath4)
        # print("message")
        # print(secret_text)
        # print(imgpath3)
        # path = open(imgpath3, 'r')
        # mime_type, _ = mimetypes.guess_type(imgpath3)
        #
        # response = HttpResponse(path, content_type=mime_type)
        # response['Content-Disposition'] = "attachment; filename=%s" % imgname3
        # return response






    return render(request,'vcrypt/message.html')
