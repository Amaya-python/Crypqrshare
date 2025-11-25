from django.urls import path, re_path
from . import views

urlpatterns = [
    path('post_complaint/', views.postcomplaint),
    path('view_complaint/', views.viewcomplaint),
    re_path(r'^post_reply/(?P<idd>\w+)$', views.postreply),
    path('view_reply/', views.viewreply),
    path('view_manager_reply/', views.viewmanagerreply),
]
