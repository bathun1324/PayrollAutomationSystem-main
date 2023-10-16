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


class PayrollAPIView(APIView):
    def get(self, request):
        sql_query = """
        SELECT *
        FROM HRM_EMPL empl
        JOIN BIM_DEPT dept
        ON empl.DEPT_NO = dept.DEPT_NO
        WHERE empl.HFFC_STATE = "O"
        ORDER BY CAST(empl.EMPL_NO AS UNSIGNED)
        """

        # SQL 쿼리 실행
        cursor = connection.cursor()
        cursor.execute(sql_query)

        payroll_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "dept_nm": row[30],  # 부서명
                "empl_no": row[2],  # 사원번호
                "empl_nm": row[4],  # 사원명
                "empl_rspofc": row[5],  # 직책
                "empl_encpnd": row[28],  # 입사일자
                "empl_salary_form": row[20],  # 급여종류
            }
            payroll_employees.append(serialized_empl)

        return JsonResponse(payroll_employees, safe=False)
