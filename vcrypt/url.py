from django.conf.urls import url
from vcrypt import views

urlpatterns = [
    url('enc/', views.encpass),
    url('dec/', views.dec_file),
    url('manager/',views.manager),
    url('employee/',views.employee)
]