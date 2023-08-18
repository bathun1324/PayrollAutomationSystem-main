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

# @login_required(login_url="/login/")
class DepartmentAPIView(APIView):
    def get(self, request):
        departments = HrmDept.objects.all()
        serialized_departments = []
        
        for dept in departments:
            state = "정상" if dept.state == "1" else "비정상"
            corp_instance = ComCorp.objects.get(pk=dept.corp_no.pk)
            corp_serializer = ComCorpSerializer(corp_instance)
            serialized_dept = {
                "no": corp_serializer.data,
                "id": dept.dept_no,
                "name": dept.dept_nm,
                "state": state,
                "reg_dtime": dept.reg_dtime,
                "reg_id": dept.reg_id,
                "upt_dtime": dept.upt_dtime,
                "upt_id": dept.upt_id
            }
            serialized_departments.append(serialized_dept)
        
        return JsonResponse(serialized_departments, safe=False)
    
class DepartmentAPIPost(APIView):
    
    def post(self, request):
        # POST 요청에서 전달된 데이터 가져오기
            data = request.data
            now = datetime.now()
            
            corp_no = '1'
            dept_name = data.get('deptName')
            dept_status = data.get('status')
            reg_date = '2023-01-10'
            reg_id = data.get('regId')
            mod_date = '2023-01-10'
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
            
class DepartmentAPIDelete(APIView):
    
    def post(self, request):
        # POST 요청에서 전달된 데이터 가져오기
            data = request.data
            corp_no = '1'
            dept_no = data.get("id")

            try:
                # 직접 SQL 문 사용하여 데이터베이스에 부서 정보 등록
                with connection.cursor() as cursor:
                    
                    sql_query = """
                    UPDATE FROM HRM_DEPT WHERE dept_no = %s AND corp_no = %s
                    """
                    cursor.execute(sql_query, [dept_no, corp_no])

                return Response({"message": "Data delete successfully"}, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"error": "error"}, status=status.HTTP_400_BAD_REQUEST)