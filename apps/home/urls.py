from django.urls import path, re_path
from apps.home import views
from django.views.generic import TemplateView
from apps.home.api.department import *
from apps.home.api.login import *
from apps.home.api.employee import *
from apps.home.api.attendance import *
from apps.home.api.commutemanage import *
from apps.home.api.employeelist import *
from apps.home.api.beacon import *

urlpatterns = [
    # management
    path('get_departments/', DepartmentAPIView.as_view()),
    path('post_departments/', DepartmentAPIPost.as_view()),
    path('delete_departments/', DepartmentAPIDelete.as_view()),
    path('search_departments/', DepartmentAPISearch.as_view()),

    # login
    path('login/', LoginAPI.as_view()),

    # employee
    path('get_employees/', EmployeeAPIView.as_view()),
    path('post_employees/', EmployeeAPIPost.as_view()),
    path('post_employeesupdate/', EmployeeupdateAPIPost.as_view()),
    path('fmly_employees/', EmployeeAPIFmly.as_view()),
    path('get_rate/', EmployeeAPIRate.as_view()),
    path('get_role/', EmployeeAPIRole.as_view()),
    path('search_employees/', EmployeeAPIViewSearch.as_view()),
    path('get_detailtable/', EmployeeAPIDetailTable.as_view()),
    path('get_detailattend/', EmployeeAPIDetailAttend.as_view()),
    path('get_detailsalary/', EmployeeAPIDetailSalary.as_view()),
    path('get_detailfrgnr/', EmployeeAPIDetailFrgnr.as_view()),
    path('get_detailtablefmly/', EmployeeAPIDetailTableFmly.as_view()),


    # attendance
    path('get_attendace/', AttendanceAPIView.as_view()),

    # commutemanage
    path('get_commutemanage/', CommuteManageAPIView.as_view()),
    path('search_commutemanage/', CommuteManageAPISearch.as_view()),

    # employeelist 직원명부
    path('get_employeelist/', EmployeelistAPIView.as_view()),
    path('search_employeelist/', EmployeelistAPISearch.as_view()),
    path('get_retireemployeelist/', RetireemployeelistAPIView.as_view()),
    path('search_retireemployeelist/', RetireemployeelistAPISearch.as_view()),
    
    # beacon 비콘
    path('get_beaconcheck/', BeaconAPIPost.as_view()),
    
]
