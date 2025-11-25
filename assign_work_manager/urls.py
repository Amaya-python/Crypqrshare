from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^post_assign_work/(?P<idd>\w+)/$', views.postassign),
    path('assign_awork/', views.compassign),
    path('view_assign_work/', views.viewassign),
    path('view_assmngr/', views.viewassmngr),
]
