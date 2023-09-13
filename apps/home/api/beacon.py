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
        SELECT *
        FROM HRM_EMPL empl, ATM_DALY daly, HRM_DEPT dept
        WHERE empl.EMPL_NO = daly.EMPL_NO AND empl.DEPT_NO = dept.DEPT_NO
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

class BeaconAPIPost(APIView):    
    def post(self, request):
        
        data = request.data
        
        print('this')
        print(data.get("atend_time"))
        
        # no = data.get("no")
        # id = data.get("id")
        # empl_no = data.get("empl_no")
        # work_date = data.get("work_date")
        # work_sch = data.get("work_sch")
        # atend_time = data.get("atend_time")
        # lvofc_time = data.get("lvofc_time")
        # gnot = data.get("gnot")
        # rtn = data.get("rtn")
        # atend_jdgmnt = data.get("atend_jdgmnt")
        # lvofc_jdgmnt = data.get("lvofc_jdgmnt")
        # laten_time = data.get("laten_time")
        # gnot_time = data.get("gnot_time")
        # elpd_atend = data.get("elpd_atend")
        # extn_work = data.get("extn_work")
        # night_work = data.get("night_work")
        # hday_work = data.get("hday_work")
        # realwork_time = data.get("realwork_time")
        # remark = data.get("remark")
        # regdtime = data.get("regdtime")
        # regid = data.get("regid")
        # uptdtime = data.get("uptdtime")
        # uptid = data.get("uptid")
        
        # corp_no = "11"
        # dept_no = "1"
        # empl_no = "1"
        # work_date = "1"
        # work_sch = "1"
        # atend_time = data.get("atend_time")
        # lvofc_time = "1"
        # gnot = "1"
        # rtn = "1"
        # atend_jdgmnt = "1"
        # lvofc_jdgmnt = "1"
        # laten_time = "1"
        # gnot_time = "1"
        # elpd_atend = "1"
        # extn_work = "1"
        # night_work = "1"
        # hday_work = "1"
        # realwork_time = "1"
        # remark = "1"
        # regdtime = "1"
        # regid = "1"
        # uptdtime = "1"
        # uptid = "1"

        # try:
        #         # 직접 SQL 문 사용하여 데이터베이스에 부서 정보 등록
        #         with connection.cursor() as cursor:
        #             # cursor.execute("SELECT MAX(DEPT_NO) FROM HRM_DEPT WHERE CORP_NO = %s", [corp_no])
        #             # max_dept_no = cursor.fetchone()[0]
        #             # new_dept_no = (max_dept_no or 0) + 1
                    
        #             sql_query = """
        #             INSERT INTO HRM_DEPT (CORP_NO, DEPT_NO, DEPT_NM, STATE, REG_DTIME, REG_ID, UPT_DTIME, UPT_ID)
        #             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        #             """
        #             cursor.execute(sql_query, [corp_no, dept_no, empl_no, work_date, work_sch, atend_time, lvofc_time, gnot])

        #         return Response({"message": "Data inserted successfully"}, status=status.HTTP_201_CREATED)

        # except Exception as e:
        #         return Response({"error": "error"}, status=status.HTTP_400_BAD_REQUEST)
    