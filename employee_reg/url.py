from django.conf.urls import url
from employee_reg import views

urlpatterns = [
    url('employee_reg/', views.employeereg),
    url('manage_employee/', views.manageemployee),
    url('view_employee/', views.viewemployee),
    url('accept/(?P<idd>\w+)', views.accept),
    url('reject/(?P<idd>\w+)', views.reject),

]