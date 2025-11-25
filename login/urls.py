from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),  # root login page
    path('forget/', views.forget_password, name='forget_password'),
]
