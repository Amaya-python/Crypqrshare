from django.conf.urls import url
from temp import views

urlpatterns = [
    url('home/', views.home),
    url('company/', views.company),
    url('manager/', views.manager),
    url('employee/', views.employee),
]