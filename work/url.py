from django.conf.urls import url
from work import views

urlpatterns = [
    url('view_work/', views.viewworkstatus),
    url('add_work/', views.addwork),
    url('update_work_status/(?P<idd>\w+)',views.updateworkstatus),
    url('view_workstatus_manager/', views.viewworkstatusmanager),
    url('update_work_status/',views.updateworkstatus),
]
