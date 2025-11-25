from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.employeereg),
    path('manage_employee/', views.manageemployee),
    path('view_employee/', views.viewemployee),

    re_path(r'^accept/(?P<idd>\w+)$', views.accept),
    re_path(r'^reject/(?P<idd>\w+)$', views.reject),
]
