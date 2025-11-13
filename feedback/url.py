from django.conf.urls import url
from feedback import views

urlpatterns = [
    url('post_complaint/', views.postcomplaint),
    url('view_complaint/', views.viewcomplaint),
    url('post_reply/(?P<idd>\w+)',views.postreply),
    url('view_reply/', views.viewreply),
    url('view_manager_reply/', views.viewmanagerreply),

]