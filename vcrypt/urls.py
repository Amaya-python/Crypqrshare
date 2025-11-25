from django.urls import path
from vcrypt import views

urlpatterns = [
    path('enc/', views.encpass),
    path('dec/', views.dec_file),
    path('manager/', views.manager),
    path('employee/', views.employee),
]
