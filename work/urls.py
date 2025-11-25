from django.urls import path, re_path
from work import views

urlpatterns = [
    path('view_work/', views.viewworkstatus),
    path('add_work/', views.addwork),

    # regex URL for idd
    path('update_work_status/<str:idd>/', views.updateworkstatus)
,

    path('view_workstatus_manager/', views.viewworkstatusmanager),

    # This path has NO id — keep it separate
    path('update_work_status/', views.updateworkstatus),
]
