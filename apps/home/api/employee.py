from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db import *

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.http import JsonResponse
from rest_framework import status

from apps.home.models import *
from apps.home.serializers import *

from datetime import datetime

class EmployeeAPIView(APIView):
    def get(self, request):
        sql_query = """
        SELECT *
        FROM HRM_EMPL empl
        JOIN HRM_DEPT dept
        ON empl.DEPT_NO = dept.DEPT_NO
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
                "empl_rspofc": row[17], # 직책
                "empl_emplym_form": row[18], # 고용형태
                "empl_encpnd": row[20], # 입사일
                "empl_hffc_state": row[21], # 재직상태
                "empl_retire_date": row[22], # 퇴사일자
                "empl_frgnr_yn": row[23], # 외국인여부
                "empl_dept_nm" : row[30], # 부서이름
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)
        
        return JsonResponse(serialized_employees, safe=False)
    
class EmployeeAPIPost(APIView):
    def post(self, request):
        # POST 요청에서 전달된 데이터 가져오기
            data = request.data
            now = datetime.now()
            
            corp_no = '1'
            dept_name = data.get('deptName')
            dept_status = data.get('status')
            reg_date = now.time()
            reg_id = data.get('regId')
            mod_date = now.time()
            mod_id = data.get('modId')

            try:
                # 직접 SQL 문 사용하여 데이터베이스에 부서 정보 등록
                with connection.cursor() as cursor:
                    cursor.execute("SELECT MAX(DEPT_NO) FROM HRM_DEPT WHERE CORP_NO = %s", [corp_no])
                    max_dept_no = cursor.fetchone()[0]
                    new_dept_no = (max_dept_no or 0) + 1
                    
                    sql_query = """
                    INSERT INTO HRM_DEPT (CORP_NO, DEPT_NO, DEPT_NM, STATE, REG_DTIME, REG_ID, UPT_DTIME, UPT_ID)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(sql_query, [corp_no, new_dept_no, dept_name, dept_status, reg_date, reg_id, mod_date, mod_id])

                return Response({"message": "Data inserted successfully"}, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"error": "error"}, status=status.HTTP_400_BAD_REQUEST)
    