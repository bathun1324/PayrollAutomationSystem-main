from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db import *
from django.db import transaction

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.http import JsonResponse
from rest_framework import status

from apps.home.models import *
from apps.home.serializers import *

from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class EmployeelistAPIView(APIView):
    def get(self, request):
        sql_query = """
        SELECT *
        FROM HRM_EMPL empl
        JOIN HRM_DEPT dept
        ON empl.DEPT_NO = dept.DEPT_NO
        JOIN HRM_SALARY sal
        ON sal.EMPL_NO = empl.EMPL_NO
        WHERE empl.HFFC_STATE IN("재직", "휴직")
        ORDER BY CAST(empl.EMPL_NO AS UNSIGNED)
        """

        # SQL 쿼리 실행
        cursor = connection.cursor()
        cursor.execute(sql_query)

        serialized_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "no": row[0],  # 회사번호
                "id": row[1],  # 부서번호
                "empl_no": row[2],  # 사원번호
                "empl_nm": row[3],  # 사원명
                "empl_ssid": row[4],  # 주민번호
                "empl_gender": row[5],  # 성별
                "empl_telno": row[11],  # 전화번호
                "empl_ssid_addr": row[12],  # 실거주지
                "empl_rspofc": row[17],  # 직책
                "empl_emplym_form": row[18],  # 고용형태
                "empl_salary_form": row[19],  # 급여형태
                "empl_encpnd": row[20],  # 입사일
                "empl_hffc_state": row[21],  # 재직상태
                "empl_retire_date": row[22],  # 퇴사일자
                "empl_frgnr_yn": row[23],  # 외국인여부
                "empl_dept_nm": row[30],  # 부서이름
                "empl_bank": row[40],  # 은행
                "empl_acc": row[41],  # 계좌번호
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)


# 직원명부>직원명부조회>검색
class EmployeelistAPISearch(APIView):
    def get(self, request):
        # url = `http://127.0.0.1:8000/search_employeelist/?employee_encpnd=${encpnd}&department_no=${deptno}&employee_rspofc=${rspofc}`
        empl_encpnd = request.GET.get('employee_encpnd', None)  # 입사일
        dept_no = request.GET.get('department_no', None)    # 부서번호
        empl_rspofc = request.GET.get('employee_rspofc', None)  # 직급

        sql_query = """
        SELECT *
        FROM HRM_EMPL empl
        JOIN HRM_DEPT dept
        ON empl.DEPT_NO = dept.DEPT_NO
        JOIN HRM_SALARY sal
        ON sal.EMPL_NO = empl.EMPL_NO
        WHERE 1=1
        """
        values = []

        if empl_encpnd and empl_encpnd != 'undefined':
            sql_query += " AND DATEDIFF( %s, empl.ENCPND) <= 0 "
            values.append(empl_encpnd)

        if dept_no and dept_no != 'undefined':
            sql_query += " AND dept.DEPT_NO = %s "
            values.append(dept_no)

        if empl_rspofc and empl_rspofc != 'undefined':
            sql_query += " AND empl.RSPOFC = %s "
            values.append(empl_rspofc)

        sql_query += " ORDER BY CAST(empl.EMPL_NO AS UNSIGNED) "

        # SQL 쿼리 실행
        cursor = connection.cursor()
        cursor.execute(sql_query, values)

        serialized_employeelist = []
        for row in cursor.fetchall():
            serialized_empl = {
                "no": row[0],  # 회사번호
                "id": row[1],  # 부서번호
                "empl_no": row[2],  # 사원번호
                "empl_nm": row[3],  # 사원명
                "empl_ssid": row[4],  # 주민번호
                "empl_gender": row[5],  # 성별
                "empl_telno": row[11],  # 전화번호
                "empl_ssid_addr": row[12],  # 실거주지
                "empl_rspofc": row[17],  # 직책
                "empl_emplym_form": row[18],  # 고용형태
                "empl_salary_form": row[19],  # 급여형태
                "empl_encpnd": row[20],  # 입사일
                "empl_hffc_state": row[21],  # 재직상태
                "empl_retire_date": row[22],  # 퇴사일자
                "empl_frgnr_yn": row[23],  # 외국인여부
                "empl_dept_nm": row[30],  # 부서이름
                "empl_bank": row[40],  # 은행
                "empl_acc": row[41],  # 계좌번호
            }
            serialized_employeelist.append(serialized_empl)

        return JsonResponse(serialized_employeelist, safe=False)


class RetireemployeelistAPIView(APIView):
    def get(self, request):
        sql_query = """
        SELECT *, ABS(TIMESTAMPDIFF(DAY, empl.ENCPND, empl.RETIRE_DATE))
        FROM HRM_EMPL empl
        JOIN HRM_DEPT dept
        ON empl.DEPT_NO = dept.DEPT_NO
        JOIN HRM_SALARY sal
        ON sal.EMPL_NO = empl.EMPL_NO AND empl.HFFC_STATE = "퇴사"
        ORDER BY CAST(empl.EMPL_NO AS UNSIGNED)
        """

        # SQL 쿼리 실행
        cursor = connection.cursor()
        cursor.execute(sql_query)

        serialized_retireemployeelist = []

        for row in cursor.fetchall():
            serialized_empl = {
                "no": row[0],  # 회사번호
                "id": row[1],  # 부서번호
                "empl_no": row[2],  # 사원번호
                "empl_nm": row[3],  # 사원명
                "empl_ssid": row[4],  # 주민번호
                "empl_gender": row[5],  # 성별
                "empl_telno": row[11],  # 전화번호
                "empl_ssid_addr": row[12],  # 실거주지
                "empl_email": row[14],  # 이메일
                "empl_rspofc": row[17],  # 직책
                "empl_emplym_form": row[18],  # 고용형태
                "empl_salary_form": row[19],  # 급여형태
                "empl_encpnd": row[20],  # 입사일
                "empl_hffc_state": row[21],  # 재직상태
                "empl_retire_date": row[22],  # 퇴사일자
                "empl_frgnr_yn": row[23],  # 외국인여부
                "empl_dept_nm": row[30],  # 부서이름
                "empl_bank": row[40],  # 은행
                "empl_acc": row[41],  # 계좌번호
                "empl_period": row[50],  # 재직기간
            }
            print(serialized_empl)
            serialized_retireemployeelist.append(serialized_empl)

        return JsonResponse(serialized_retireemployeelist, safe=False)


# 직원명부>직원명부조회>검색
class RetireemployeelistAPISearch(APIView):
    def get(self, request):
        # `http://127.0.0.1:8000/search_retireemployeelist/?encpnd=${searchtext.encpnd}&retire_date=${searchtext.retire_date}&dept_id=${searchtext.dept_id}`
        empl_encpnd = request.GET.get('encpnd', None)  # 입사일
        retire_date = request.GET.get('retire_date', None)    # 퇴사일
        dept_no = request.GET.get('dept_id', None)  # 부서번호

        sql_query = """
        SELECT *, ABS(TIMESTAMPDIFF(DAY, empl.ENCPND, empl.RETIRE_DATE))
        FROM HRM_EMPL empl
        JOIN HRM_DEPT dept
        ON empl.DEPT_NO = dept.DEPT_NO
        JOIN HRM_SALARY sal
        ON sal.EMPL_NO = empl.EMPL_NO
        WHERE empl.HFFC_STATE = "퇴사"
        """
        values = []

        if empl_encpnd and empl_encpnd != 'undefined':
            # 선택한 입사일 이후에 입사한 직원 출력
            sql_query += " AND DATEDIFF( %s, empl.ENCPND) <= 0 "
            values.append(empl_encpnd)

        if retire_date and retire_date != 'undefined':
            # 선택한 퇴사일 이전에 퇴사한 직원 출력
            sql_query += " AND DATEDIFF( %s, empl.RETIRE_DATE) >= 0  "
            values.append(retire_date)

        if dept_no and dept_no != 'undefined':
            sql_query += " AND dept.DEPT_NO = %s "
            values.append(dept_no)

        sql_query += " ORDER BY CAST(empl.EMPL_NO AS UNSIGNED) "

        # SQL 쿼리 실행
        cursor = connection.cursor()
        cursor.execute(sql_query, values)

        serialized_employeelist = []
        for row in cursor.fetchall():
            serialized_empl = {
                "no": row[0],  # 회사번호
                "id": row[1],  # 부서번호
                "empl_no": row[2],  # 사원번호
                "empl_nm": row[3],  # 사원명
                "empl_ssid": row[4],  # 주민번호
                "empl_gender": row[5],  # 성별
                "empl_telno": row[11],  # 전화번호
                "empl_ssid_addr": row[12],  # 실거주지
                "empl_email": row[13],  # 이메일
                "empl_rspofc": row[17],  # 직책
                "empl_emplym_form": row[18],  # 고용형태
                "empl_salary_form": row[19],  # 급여형태
                "empl_encpnd": row[20],  # 입사일
                "empl_hffc_state": row[21],  # 재직상태
                "empl_retire_date": row[22],  # 퇴사일자
                "empl_frgnr_yn": row[23],  # 외국인여부
                "empl_dept_nm": row[30],  # 부서이름
                "empl_bank": row[40],  # 은행
                "empl_acc": row[41],  # 계좌번호
                "empl_period": row[50],  # 재직기간
            }
            serialized_employeelist.append(serialized_empl)

        return JsonResponse(serialized_employeelist, safe=False)
