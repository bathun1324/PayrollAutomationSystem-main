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


class CodeEmploymentTypeAPIView(APIView):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM CMM_CODE WHERE LCODE = '0010' AND SCODE != '0000'")
        serialized_cmmcode = []

        for row in cursor.fetchall():
            serialized_code = {
                "lcode": row[0],
                "scode": row[1],
                "cd_val": row[2],
                "desc": row[3],
                "seq": row[4],
                "reg_dtime": row[5],
                "reg_id": row[6],
                "upt_dtime": row[7],
                "upt_id": row[8],
            }
            print(serialized_code)
            serialized_cmmcode.append(serialized_code)

        return JsonResponse(serialized_cmmcode, safe=False)


class CodeSalaryFormAPIView(APIView):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM CMM_CODE WHERE LCODE = '0008' AND SCODE != '0000'")
        serialized_cmmcode = []

        for row in cursor.fetchall():
            serialized_code = {
                "lcode": row[0],
                "scode": row[1],
                "cd_val": row[2],
                "desc": row[3],
                "seq": row[4],
                "reg_dtime": row[5],
                "reg_id": row[6],
                "upt_dtime": row[7],
                "upt_id": row[8],
            }
            print(serialized_code)
            serialized_cmmcode.append(serialized_code)

        return JsonResponse(serialized_cmmcode, safe=False)


class CodeTrnBankAPIView(APIView):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM CMM_CODE WHERE LCODE = '0011' AND SCODE != '0000'")
        serialized_cmmcode = []

        for row in cursor.fetchall():
            serialized_code = {
                "lcode": row[0],
                "scode": row[1],
                "cd_val": row[2],
                "desc": row[3],
                "seq": row[4],
                "reg_dtime": row[5],
                "reg_id": row[6],
                "upt_dtime": row[7],
                "upt_id": row[8],
            }
            print(serialized_code)
            serialized_cmmcode.append(serialized_code)

        return JsonResponse(serialized_cmmcode, safe=False)


class CodeFmlyReltnAPIView(APIView):
    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM CMM_CODE WHERE LCODE = '0012' AND SCODE != '0000'")
        serialized_cmmcode = []

        for row in cursor.fetchall():
            serialized_code = {
                "lcode": row[0],
                "scode": row[1],
                "cd_val": row[2],
                "desc": row[3],
                "seq": row[4],
                "reg_dtime": row[5],
                "reg_id": row[6],
                "upt_dtime": row[7],
                "upt_id": row[8],
            }
            print(serialized_code)
            serialized_cmmcode.append(serialized_code)

        return JsonResponse(serialized_cmmcode, safe=False)
