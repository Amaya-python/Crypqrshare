from django.conf.urls import url
from login import views

urlpatterns = [
    url('login/', views.login),
    url('forget/', views.forget_password),

]
