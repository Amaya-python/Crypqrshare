from django.contrib import admin
from django.urls import path, include
from temp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('assign_work_employee/', include('assign_work_employee.urls')),
    path('assign_work_manager/', include('assign_work_manager.urls')),

    path('feedback/', include('feedback.urls')),
    path('employee_reg/', include('employee_reg.urls')),
    path('login/', include('login.urls')),
    path('manager_reg/', include('manager_reg.urls')),
    path('work/', include('work.urls')),
    path('temp/', include('temp.urls')),
    path('vcrypt/', include('vcrypt.urls')),

    path('', views.home),
]
