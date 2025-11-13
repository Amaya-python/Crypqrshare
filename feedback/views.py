from django.shortcuts import render
from feedback.models import Feedback
# Create your views here.

def postcomplaint(request):
    ss=request.session["u_id"]
    if request.method == 'POST':
        obj = Feedback()
        obj.complaint = request.POST.get('complaint')
        obj.reply = 'pending'
        obj.comp_id = 1
        obj.emp_id = ss
        obj.save()

    return render(request, 'complaint/post_complaint.html')


def postreply(request,idd):
    if request.method == 'POST':
        obj = Feedback.objects.get(complaint_id=idd)
        obj.reply = request.POST.get('reply')
        obj.save()
        return viewcomplaint(request)

    return render(request, 'complaint/post_reply.html')


def viewmanagerreply(request):
    obj =Feedback.objects.all()
    context = {
        'c': obj
    }
    return render(request, 'complaint/view_manager_reply.html',context)


def viewcomplaint(request):
    obj = Feedback.objects.all()
    context = {
        'a': obj
    }
    return render(request, 'complaint/view_complaint.html',context)


def viewreply(request):
    ss=request.session["u_id"]
    obj = Feedback.objects.filter(emp_id=ss)
    context = {
        'b': obj
    }
    return render(request, 'complaint/view_reply.html',context)





