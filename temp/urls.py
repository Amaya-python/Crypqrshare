from django.urls import path
from temp import views

urlpatterns = [
    path('home/', views.home),
    path('company/', views.company),
    path('manager/', views.manager),
    path('employee/', views.employee),
]
