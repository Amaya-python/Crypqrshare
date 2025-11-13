from django.conf.urls import url
from assign_work_manager import views

urlpatterns = [
    url('post_assign_work/(?P<idd>\w+)', views.postassign),
    url('assign_awork/', views.compassign),
    url('view_assign_work/', views.viewassign),
    url('view_assmngr/', views.viewassmngr)
]