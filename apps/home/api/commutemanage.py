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

class CommuteManageAPIView(APIView):
    def get(self, request):
        sql_query = """
        SELECT *
        FROM HRM_EMPL empl, HRM_ATEND atend, HRM_DEPT dept
        WHERE empl.EMPL_NO = atend.EMPL_NO AND empl.DEPT_NO = dept.DEPT_NO
        """

        # SQL 쿼리 실행
        cursor = connection.cursor()
        cursor.execute(sql_query)
        
        serialized_employees = []
        
        for row in cursor.fetchall():
            serialized_empl = {
                "no": row[0], # 회사번호
                "id": row[1], # 부서번호
                "empl_no": row[2], # 사원번호
                "empl_nm": row[3], # 사원명
                "empl_ssid": row[4], # 주민번호
                "empl_gender": row[5], # 성별
                "empl_telno": row[11], # 전화번호
                "empl_ssid_addr": row[12], # 주민번호주소
                "empl_tltsdnc_addr": row[13], # 실거주지주소
                "empl_rspofc": row[17], # 직책
                "empl_emplym_form": row[18], # 고용형태
                "empl_salary_form": row[19], # 급여형태
                "empl_encpnd": row[20], # 입사일
                "empl_hffc_state": row[21], # 재직상태
                "empl_retire_date": row[22], # 퇴사일자
                "empl_frgnr_yn": row[23], # 외국인여부
                "empl_base_atendtime" : row[31], # 기본출근시간
                "empl_base_lvofctime" : row[32], # 기본퇴근시간
                "empl_dept_nm" : row[40], # 부서명
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)
        
        return JsonResponse(serialized_employees, safe=False)