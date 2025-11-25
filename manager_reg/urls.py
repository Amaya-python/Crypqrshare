from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.managerreg),
    path('update_profile/', views.updatemanagerprofile),
    re_path(r'^profile_view_manager/(?P<idd>\w+)$', views.profileviewmanager),
    re_path(r'^delete/(?P<idd>\w+)$', views.delete),
    path('view_manager/', views.viewmanager),
    path('co/', views.comp),
]
