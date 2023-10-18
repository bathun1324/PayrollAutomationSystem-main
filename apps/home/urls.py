from django.urls import path, re_path
from apps.home import views
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.home.api.department import *
from apps.home.api.login import *
from apps.home.api.employee import *
from apps.home.api.attendance import *
from apps.home.api.commutemanage import *
from apps.home.api.employeelist import *
from apps.home.api.beacon import *
from apps.home.api.payroll import *
from apps.home.api.corporation import *
from apps.home.api.code import *

urlpatterns = [
    # JWT Token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

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
    path('search_attendace/', AttendanceAPISearch.as_view()),

    # commutemanage
    path('get_commutemanage/', CommuteManageAPIView.as_view()),
    path('search_commutemanage/', CommuteManageAPISearch.as_view()),

    # employeelist 직원명부
    path('get_employeelist/', EmployeelistAPIView.as_view()),
    path('search_employeelist/', EmployeelistAPISearch.as_view()),
    path('get_retireemployeelist/', RetireemployeelistAPIView.as_view()),
    path('search_retireemployeelist/', RetireemployeelistAPISearch.as_view()),

    # payroll 급여관리
    path('get_payroll/', PayrollAPIView.as_view()),


    # beacon 비콘
    path('get_beaconcheck/', BeaconAPIView.as_view()),
    path('post_beaconcheck/', BeaconAPIPost.as_view()),
    path('post_beaconcheck_ex/', BeaconAPIPostEx.as_view()),

    # corporation 회사정보
    path('get_corporationinfo/', CorporationInfoAPIView.as_view()),
    path('search_corporationinfo/', CorporationInfoAPISearch.as_view()),
    path('post_corporation/', CorporationAPIPost.as_view()),
    path('get_info/', CorporationGetInfo.as_view()),
    path('get_ofcps/', CorporationGetOfcps.as_view()),


    # cmm_code 공통코드
    path('get_codeEmploymentType/', CodeEmploymentTypeAPIView.as_view()),
]
