from django.urls import path
from assign_work_employee import views

urlpatterns = [
    path('post_assign_work/<str:idd>/', views.postassignwork),
    path('ass/', views.assignwork),
    path('as_view/', views.viewassignwork),
    path('upp/<str:idd>/', views.sts_upd),
    path('view_co/', views.comp),
]
