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


class CorporationInfoAPIView(APIView):
    def get(self, request):
        
        cmpy_detail = request.GET.get('cmpy_detail', None)
        
        if(cmpy_detail):
            sql_query = """
            SELECT * FROM COM_CORP a, COM_CNTRCT b WHERE a.CORP_NO = b.CORP_NO WHERE a.CORP_NO = """ + cmpy_detail + """
            """         
        else:
            sql_query = """
            SELECT * FROM COM_CORP a, COM_CNTRCT b WHERE a.CORP_NO = b.CORP_NO 
            """
        


        # SQL 쿼리 실행
        cursor = connection.cursor()
        cursor.execute(sql_query)

        serialized_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "corp_no": row[0],
                "corp_nm": row[1],
                "repre_no": row[2],
                "bizm_no": row[3],
                "repre_telno": row[4],
                "addr": row[5],
                "empl_num": row[6],
                "logo_id": row[7],
                "mngr_nm": row[8],
                "rspofc": row[9],
                "corp_telno": row[10],
                "email": row[11],
                "mobile_no": row[12],
                "mngr_id": row[13],
                "mtyvc_stl_std": row[14],
                "tml_use_yn": row[15],
                "remark": row[16],
                "reg_dtime": row[17],
                "reg_id": row[18],
                "upt_dtime": row[19],
                "upt_id": row[20],
                "cntrct_form": row[22],
                "state": row[23],
                "cntrct_date": row[24],
                "exp_date": row[25],
                "pmt_date": row[26],
                "ter_date": row[27],
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)
    
class CorporationInfoAPISearch(APIView):
    def get(self, request):
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        corp_nm = request.GET.get('corp_nm', None)
        
        print(start_date)
        print(end_date)
        print(corp_nm)

        values = []

        sql_query = """
            SELECT * FROM COM_CORP a, COM_CNTRCT b WHERE a.CORP_NO = b.CORP_NO 
            """
            
        if start_date and start_date != 'undefined' and end_date and end_date != 'undefined':
            sql_query += " AND CNTRCT_DATE > %s AND CNTRCT_DATE < %s "
            values.append(start_date)
            values.append(end_date)
            
        if corp_nm and corp_nm != 'undefined':
            sql_query += " AND CORP_NM = %s "
            values.append(corp_nm)
            
        # SQL 쿼리 실행
        sql_query += """ ORDER BY CNTRCT_DATE DESC """
        cursor = connection.cursor()
        cursor.execute(sql_query, values)

        serialized_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "corp_no": row[0],
                "corp_nm": row[1],
                "repre_no": row[2],
                "bizm_no": row[3],
                "repre_telno": row[4],
                "addr": row[5],
                "empl_num": row[6],
                "logo_id": row[7],
                "mngr_nm": row[8],
                "rspofc": row[9],
                "corp_telno": row[10],
                "email": row[11],
                "mobile_no": row[12],
                "mngr_id": row[13],
                "mtyvc_stl_std": row[14],
                "tml_use_yn": row[15],
                "remark": row[16],
                "reg_dtime": row[17],
                "reg_id": row[18],
                "upt_dtime": row[19],
                "upt_id": row[20],
                "cntrct_form": row[22],
                "state": row[23],
                "cntrct_date": row[24],
                "exp_date": row[25],
                "pmt_date": row[26],
                "ter_date": row[27],
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)
            
        return JsonResponse(serialized_employees, safe=False)
    
class CorporationDetailInfoAPIView(APIView):
    def get(self, request):

        cmpy_detail = request.GET.get('cmpy_detail', None)

        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM COM_CORP a, COM_CNTRCT b WHERE a.CORP_NO = b.CORP_NO AND a.CORP_NO = %s", [cmpy_detail])

        serialized_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "corp_no": row[0],
                "corp_nm": row[1],
                "repre_no": row[2],
                "bizm_no": row[3],
                "repre_telno": row[4],
                "addr": row[5],
                "empl_num": row[6],
                "logo_id": row[7],
                "mngr_nm": row[8],
                "rspofc": row[9],
                "corp_telno": row[10],
                "email": row[11],
                "mobile_no": row[12],
                "mngr_id": row[13],
                "mtyvc_stl_std": row[14],
                "tml_use_yn": row[15],
                "remark": row[16],
                "reg_dtime": row[17],
                "reg_id": row[18],
                "upt_dtime": row[19],
                "upt_id": row[20],
                "cntrct_form": row[22],
                "state": row[23],
                "cntrct_date": row[24],
                "exp_date": row[25],
                "pmt_date": row[26],
                "ter_date": row[27],
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)