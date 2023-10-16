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
        FROM HRM_EMPL empl, ATM_DALY daly, BIM_DEPT dept
        WHERE empl.EMPL_NO = daly.EMPL_NO AND empl.DEPT_NO = dept.DEPT_NO ORDER BY ATEND_TIME DESC
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
                "empl_gender": row[5], # 성별
                "empl_frgnr_yn": row[23], # 외국인여부
                "empl_work_date": row[31], # 근무일자
                "empl_work_sch": row[32], # 스케쥴
                "empl_atend_time": row[33], # 출근일자
                "empl_lvofc_time": row[34], # 퇴근일자
                "empl_atend_jdgmnt": row[37], # 출근판정
                "empl_lvofc_jdgmnt": row[38], # 퇴근판정
                "empl_extn_work": row[42], # 연장근무
                "empl_realwork_tume": row[45], # 실제근무
                "empl_remark": row[46], # 비고
                "empl_dept_nm": row[53], # 부서이름
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)

# 출퇴근 확인 및 조회 검색


class CommuteManageAPISearch(APIView):
    def get(self, request):
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        department = request.GET.get('department', None)
        attendyn = request.GET.get('attendyn', None)
        
        print(start_date)
        print(end_date)
        print(department)
        print(attendyn)

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
            
        if attendyn and attendyn != 'undefined':
            if attendyn == '출근':
                sql_query += " AND daly.ATEND_JDGMNT = %s "
                values.append(attendyn)
            elif attendyn == '퇴근':
                sql_query += " AND daly.LVOFC_JDGMNT = %s "
                values.append(attendyn)
            
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
                "empl_atend_jdgmnt": row[37], # 출근판정
                "empl_lvofc_jdgmnt": row[38], # 퇴근판정
                "empl_extn_work": row[42], # 연장근무
                "empl_realwork_tume": row[45], # 실제근무
                "empl_remark": row[46], # 비고
                "empl_dept_nm": row[53], # 부서이름
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)
