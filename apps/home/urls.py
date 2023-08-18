from django.urls import path, re_path
from apps.home import views
from django.views.generic import TemplateView
from apps.home.api.management import *
from apps.home.api.login import *
from apps.home.api.employee import *

urlpatterns = [
    # management
    path('get_departments/', DepartmentAPIView.as_view()),
    path('post_departments/', DepartmentAPIPost.as_view()),
    #path('delete_departments/', DepartmentAPIDelete.as_view()),
    
    # login
    path('login/', LoginAPI.as_view()),
    
    # employee
    path('get_employees/', EmployeeAPIView.as_view()),
    path('post_employees/', EmployeeAPIPost.as_view()),
    path('max_employees/', EmployeeAPIMax.as_view()),
    path('fmly_employees/', EmployeeAPIFmly.as_view()),
]
