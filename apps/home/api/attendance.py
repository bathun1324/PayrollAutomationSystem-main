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

class AttendanceAPIView(APIView):
    def get(self, request):
        
        sql_query = """
        SELECT * FROM ATM_DALY daly
        INNER JOIN HRM_EMPL empl
        ON empl.EMPL_NO = daly.EMPL_NO
        INNER JOIN BIM_DEPT dept
        ON dept.DEPT_NO = daly.DEPT_NO AND daly.CORP_NO = dept.CORP_NO
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
                "empl_nm": row[28], # 사원명
                "empl_gender": row[5], # 성별
                "empl_frgnr_yn": row[37], # 외국인여부
                "empl_work_date": row[32], # 근무일자
                "empl_work_sch": row[4], # 스케쥴
                "empl_atend_time": row[5], # 출근일자
                "empl_lvofc_time": row[6], # 퇴근일자
                "empl_gnot": row[36], # 외출시간
                "empl_rtn": row[37], # 복귀시간
                "empl_atend_jdgmnt": row[9], # 출근판정
                "empl_lvofc_jdgmnt": row[10], # 퇴근판정
                "empl_laten_time": row[40], # 지각시간
                "empl_gnot_time": row[41], # 외출시간
                "empl_elpd_atend": row[42], # 조기추근
                "empl_extn_work": row[14], # 연장근무
                "empl_night_work": row[44], # 야간근무
                "empl_hday_work": row[45], # 휴일근무
                "empl_realwork_tume": row[17], # 실제근무
                "empl_remark": row[18], # 비고
                "empl_dept_nm": row[55], # 부서이름
            }
            serialized_employees.append(serialized_empl)
        
        return JsonResponse(serialized_employees, safe=False)

class AttendanceAPISearch(APIView):
    def get(self, request):
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        department = request.GET.get('department', None)
        
        print(start_date)
        print(end_date)
        print(department)

        values = []

        sql_query = """
            SELECT *
            FROM HRM_EMPL empl, ATM_DALY daly, BIM_DEPT dept
            WHERE empl.EMPL_NO = daly.EMPL_NO AND empl.DEPT_NO = dept.DEPT_NO
            """
            
        if start_date and start_date != 'undefined' and end_date and end_date != 'undefined':
            sql_query += " AND ATEND_TIME > %s AND ATEND_TIME < %s "
            values.append(start_date)
            values.append(end_date)
            
        if department and department != 'undefined':
            sql_query += " AND dept.DEPT_NM = %s "
            values.append(department)
            
        # SQL 쿼리 실행
        sql_query += """ ORDER BY ATEND_TIME DESC """
        cursor = connection.cursor()
        cursor.execute(sql_query, values)

        serialized_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "no": row[0], # 회사번호
                "id": row[1], # 부서번호
                "empl_no": row[2], # 사원번호
                "empl_nm": row[3], # 사원명
                "empl_gender": row[5], # 성별
                "empl_frgnr_yn": row[23], # 외국인여부
                "empl_work_date": row[31], # 근무일자
                "empl_work_sch": row[32], # 스케쥴
                "empl_atend_time": row[33], # 출근일자
                "empl_lvofc_time": row[34], # 퇴근일자
                "empl_gnot": row[35], # 외출시간
                "empl_rtn": row[36], # 복귀시간
                "empl_atend_jdgmnt": row[37], # 출근판정
                "empl_lvofc_jdgmnt": row[38], # 퇴근판정
                "empl_laten_time": row[39], # 지각시간
                "empl_gnot_time": row[40], # 외출시간
                "empl_elpd_atend": row[41], # 조기추근
                "empl_extn_work": row[42], # 연장근무
                "empl_night_work": row[43], # 야간근무
                "empl_hday_work": row[44], # 휴일근무
                "empl_realwork_tume": row[45], # 실제근무
                "empl_remark": row[46], # 비고
                "empl_dept_nm": row[53], # 부서이름
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)