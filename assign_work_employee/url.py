from django.conf.urls import url
from assign_work_employee import views

urlpatterns = [
    url('post_assign_work/(?P<idd>\w+)', views.postassignwork),
    url('ass/', views.assignwork),
    url('as_view/', views.viewassignwork),
    url('upp/(?P<idd>\w+)', views.sts_upd),
    url('view_co/', views.comp)
]