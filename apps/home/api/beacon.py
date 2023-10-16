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

class BeaconAPIView(APIView):
    def get(self, request):
        sql_query = """
        SELECT *
        FROM HRM_EMPL empl, ATM_DALY daly, BIM_DEPT dept
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
        
        now = datetime.now()
        works= now.strftime('%Y-%m-%d')
        work_dates = now.strftime('%Y-%m-%d %H:%M:%S')
        
        data = request.data
        
        corp_no = int(data.get("corp_no"))
        dept_no = int(data.get("dept_no"))
        empl_no = data.get("empl_no")
        work_date = works
        work_sch = data.get("work_sch")
        atend_time = work_dates
        lvofc_time = work_dates
        gnot = data.get("gnot")
        rtn = data.get("rtn")
        atend_jdgmnt = '출근'
        lvofc_jdgmnt = '퇴근'
        laten_time = data.get("laten_time")
        gnot_time = data.get("gnot_time")
        elpd_atend = data.get("elpd_atend")
        extn_work = data.get("extn_work")
        night_work = data.get("night_work")
        hday_work = data.get("hday_work")
        realwork_time = data.get("realwork_time")
        remark = data.get("remark")
        regdtime = work_dates
        regid = data.get("regid")
        uptdtime = work_dates
        uptid = data.get("uptid")
        
        print(corp_no)
        print(dept_no)

        try:
                # 직접 SQL 문 사용하여 데이터베이스에 부서 정보 등록
                with connection.cursor() as cursor:
                    cursor.execute("SELECT WORK_DATE, ATEND_TIME FROM ATM_DALY WHERE EMPL_NO = %s AND WORK_DATE = %s", [empl_no, works])
                    result = cursor.fetchone()
                    # max_dept_no = cursor.fetchone()[0]
                    # new_dept_no = (max_dept_no or 0) + 1
                    
                    # times = result[1]
                    
                    sql_query = " INSERT INTO ATM_DALY VALUES (%s, %s, %s, %s, %s, %s, null, null, null, %s, null, null, null, null, null, null, null, null, %s, %s, %s, %s, %s)"
                    cursor.execute(sql_query, [corp_no, dept_no, empl_no, work_date, work_sch, atend_time, atend_jdgmnt, remark, regdtime,
                                        regid, uptdtime, uptid])

                return Response({"message":"Data inserted successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
                return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

class BeaconAPIPostEx(APIView):
    def post(self, request):
        
        now = datetime.now()
        works= now.strftime('%Y-%m-%d')
        work_dates = now.strftime('%Y-%m-%d %H:%M:%S')
        
        data = request.data
        
        corp_no = int(data.get("corp_no"))
        dept_no = int(data.get("dept_no"))
        empl_no = data.get("empl_no")
        work_date = works
        work_sch = data.get("work_sch")
        atend_time = work_dates
        lvofc_time = work_dates
        gnot = data.get("gnot")
        rtn = data.get("rtn")
        atend_jdgmnt = '출근'
        lvofc_jdgmnt = '퇴근'
        laten_time = data.get("laten_time")
        gnot_time = data.get("gnot_time")
        elpd_atend = data.get("elpd_atend")
        extn_work = data.get("extn_work")
        night_work = data.get("night_work")
        hday_work = data.get("hday_work")
        realwork_time = data.get("realwork_time")
        remark = data.get("remark")
        regdtime = work_dates
        regid = data.get("regid")
        uptdtime = work_dates
        uptid = data.get("uptid")
        
        print(corp_no)
        print(dept_no)

        try:
                # 직접 SQL 문 사용하여 데이터베이스에 부서 정보 등록
                with connection.cursor() as cursor:
                    cursor.execute("SELECT WORK_DATE, ATEND_TIME FROM ATM_DALY WHERE EMPL_NO = %s AND WORK_DATE = %s", [empl_no, works])
                    result = cursor.fetchone()
                    # max_dept_no = cursor.fetchone()[0]
                    # new_dept_no = (max_dept_no or 0) + 1
                    
                    # times = result[1]
                    
                    sql_query = " UPDATE ATM_DALY SET LVOFC_TIME = %s, LVOFC_JDGMNT = %s, UPT_DTIME = %s, UPT_ID = %s WHERE EMPL_NO = %s AND WORK_DATE = %s"
                    cursor.execute(sql_query, [lvofc_time, lvofc_jdgmnt, uptdtime, uptid, empl_no, works])

                return Response({"message":"Data inserted successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
                return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)