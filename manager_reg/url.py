from django.conf.urls import url
from manager_reg import views

urlpatterns = [
    url('manager_reg/', views.managerreg),
    url('update_profile/', views.updatemanagerprofile),
    url('profile_view_manager/(?P<idd>\w+)', views.profileviewmanager),
    url('delete/(?P<idd>\w+)', views.delete),
    url('view_manager/', views.viewmanager),
    url('co/', views.comp)

]
