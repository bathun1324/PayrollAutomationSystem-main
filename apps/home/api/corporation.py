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
                "repre_nm": row[2],
                "bizm_no": row[3],
                "repre_telno": row[4],
                "addr": row[5],
                "empl_num": row[6],
                "mngr_nm": row[7],
                "rspofc": row[8],
                "corp_telno": row[9],
                "email": row[10],
                "mobile_no": row[11],
                "mngr_id": row[12],
                "cntrct_form": row[24],
                "state": row[25],
                "cntrct_date": row[26],
                "exp_date": row[27],
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
                "repre_nm": row[2],
                "bizm_no": row[3],
                "repre_telno": row[4],
                "addr": row[5],
                "empl_num": row[6],
                "mngr_nm": row[7],
                "rspofc": row[8],
                "corp_telno": row[9],
                "email": row[10],
                "mobile_no": row[11],
                "mngr_id": row[12],
                "cntrct_form": row[24],
                "state": row[25],
                "cntrct_date": row[26],
                "exp_date": row[27],
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
    
    
class CorporationAPIPost(APIView):
    def post(self, request):
        # POST 요청에서 전달된 데이터 가져오기
        data = request.data
        now = datetime.now()

        corporation_info = data.get('corporationinfo')
        cntrct_info = data.get('cntrctinfo')

        print(corporation_info)
        print(cntrct_info)

        # HRM_EMPL 테이블
        corp_no_empl = corporation_info.get('corp_no')  # 세션처리예정
        corp_nm_empl = corporation_info.get('corp_nm')
        repre_nm_empl = corporation_info.get('repre_nm')
        repre_telno_empl = corporation_info.get('repre_telno')
        bizm_no_empl = corporation_info.get('bizm_no')
        addr_empl = corporation_info.get('addr')
        empl_num_empl = corporation_info.get('empl_num')
        mngr_nm_empl = corporation_info.get('mngr_nm')
        ofcps_empl = corporation_info.get('ofcps')
        corp_telno_empl = corporation_info.get('corp_telno')
        email_empl = corporation_info.get('email')
        mobile_no_empl = corporation_info.get('mobile_no')
        mngr_id_empl = corporation_info.get('mngr_id')
        dept_info = corporation_info.get('info1')
        ofcps_info = corporation_info.get('info2')
        atend_info = corporation_info.get('info3')
        salary_info = corporation_info.get('info4')
        #logo_id = corporation_info.get('logo_id')
        logo_id = '1'
        #remark = corporation_info.get('remark')
        remark = '1'
        gen1 = now.strftime('%Y-%m-%d %H:%M:%S')
        gen2 = corporation_info.get('gen2')
        upt1 = now.strftime('%Y-%m-%d %H:%M:%S')
        upt2 = corporation_info.get('gen2')
        
        
        # HRM_ATEND 테이블
        # empl_no_atend = '1' #필요없음
        corp_no_cntrct = corporation_info.get('corp_no')  # 세션처리예정
        cntrct_form = corporation_info.get('cntrct_form')  # 세션처리예정
        state = cntrct_info.get('state')
        cntcrt_date = cntrct_info.get('cntcrt_date')
        exp_date = cntrct_info.get('exp_date')
        pmt_date = cntrct_info.get('pmt_date')
        ter_date = cntrct_info.get('ter_date')
        tml_use_yn = cntrct_info.get('tml_use_yn')
        exp_date = cntrct_info.get('exp_date')
        mtyvc_stl_std = cntrct_info.get('mtyvc_stl_std')

        corp_no = 1
        dept_count = 1001
        ofcps_count = 0
        salary_count = 0
        atend_count = 0
        dept_name = ['총무부', '경리부', '품질관리부', '생산1팀', '생산2팀', '기술부', '영업부']
        ofcps_name = ['대표이사', '부장', '과장', '대리', '사원']
        salary_name = ['기본급', '야간근로수당', '연장근로수당', '연차수당', '국민연금', '건강보험', '소득세', '급여지급일', '급여형태']
        atend_name = ['기본주휴일', '소정근로시간', '정상근무시간', '석식시간', '중식시간', '야식시간', '교대근무시간', '심야근무시간', '연장근무 제외시간', '연장근무 최대시간', '근무시간 최소단위']
        empl_no = corporation_info.get('empl_no')  # 사원번호
        
        try:
            # 직접 SQL 문 사용하여 데이터베이스에 부서 정보 등록
            with transaction.atomic():
                with connection.cursor() as cursor:

                    cursor.execute(
                        "SELECT MAX(CORP_NO)+1 FROM COM_CORP")
                    max_num = cursor.fetchone()[0]
                    
                    cursor.execute(
                        "SELECT IF (MAX(CAST(EMPL_NO AS UNSIGNED)) IS NULL, 1, MAX(CAST(EMPL_NO AS UNSIGNED))+1) FROM HRM_EMPL WHERE CORP_NO = %s", [corp_no_empl])
                    empl_max_num = cursor.fetchone()[0]
                    
                    cursor.execute(
                        "SELECT * FROM COM_SALARYLST")
                    empl_salary = cursor.fetchall()
                    
                    cursor.execute(
                        "SELECT * FROM COM_ATENDLST")
                    empl_atend = cursor.fetchall()

                    sql_query = """
                                    INSERT INTO COM_CORP (
                                        CORP_NO, CORP_NM, REPRE_NM, BIZM_NO, REPRE_TELNO, ADDR, EMPL_NUM, MNGR_NM, OFCPS, CORP_TELNO, EMAIL, MOBILE_NO, MNGR_ID, `DEPT INFO`, `OFCPS INFO`, `ATEND INFO`, `SALARY INFO`, LOGO_ID, REMARK, REG_DTIME, REG_ID, UPT_DTIME, UPT_ID)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                """
                    cursor.execute(sql_query, [
                        max_num, corp_nm_empl, repre_nm_empl, repre_telno_empl, bizm_no_empl, addr_empl, empl_num_empl, mngr_nm_empl, ofcps_empl, corp_telno_empl, email_empl, mobile_no_empl, mngr_id_empl, dept_info, ofcps_info, atend_info, salary_info, logo_id, remark, gen1, gen2, upt1, upt2
                    ])

                    sql_query_cntrct = """
                                        INSERT INTO COM_CNTRCT (
                                            CORP_NO, CNTRCT_FORM, STATE, CNTRCT_DATE, EXP_DATE, PMT_DATE, TER_DATE, MTYVC_STL_STD, TML_USE_YN, UPT_DTIME, UPT_ID)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                        """
                    cursor.execute(sql_query_cntrct, [
                        max_num, cntrct_form, state, cntcrt_date,
                        exp_date, pmt_date, ter_date, mtyvc_stl_std, tml_use_yn, upt1, gen2
                    ])
                    
                    sql_query_empl = """
                                        INSERT INTO HRM_EMPL (
                                            CORP_NO, DEPT_NO, EMPL_NO, EMPL_NM, OFCPS, PRSL_EMAIL, TEL_NO, MOBILE_NO, REG_DTIME, REG_ID, UPT_DTIME, UPT_ID)
                                        VALUES (%s, 1001, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                        """
                    cursor.execute(sql_query_empl, [
                        max_num, empl_max_num, corp_nm_empl, ofcps_empl, email_empl, corp_telno_empl, mobile_no_empl, gen1, gen2, upt1, gen2
                    ])
                    
                    # sql_query_emplhis = """
                    #                     INSERT INTO HRM_EMPLHIS (
                    #                         CORP_NO, DEPT_NO, EMPL_NO, EMPL_NM, OFCPS, PRSL_EMAIL, TEL_NO, MOBILE_NO, REG_DTIME, REG_ID, UPT_DTIME, UPT_ID)
                    #                     VALUES (%s, 1001, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    #                     """
                    # cursor.execute(sql_query_emplhis, [
                    #     max_num, empl_max_num, corp_nm_empl, ofcps_empl, email_empl, corp_telno_empl, mobile_no_empl, gen1, gen2, upt1, gen2
                    # ])
                        
                    sql_query_login = """
                                        INSERT INTO CMM_LOGIN (
                                            LOGIN_ID, LOGIN_PWD, PERM_ID, EMPL_NO, CORP_NO, DEPT_NO, REG_DTIME, REG_ID, UPT_DTIME, UPT_ID)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                        """
                    cursor.execute(sql_query_login, [
                        mngr_id_empl, mngr_id_empl, '11', '1', max_num, '1001', gen1, gen2, upt1, gen2
                    ])
                    
                    for dept_count in range(1001, 1008):
                        sql_query_dpet = """
                                            INSERT INTO BIM_DEPT (
                                                CORP_NO, DEPT_NO, DEPT_NM, STATE, REG_DTIME, REG_ID, UPT_DTIME, UPT_ID)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                            """
                        cursor.execute(sql_query_dpet, [
                            max_num, dept_count, dept_name[dept_count-1001], '1', gen1, gen2, upt1, gen2
                        ])
                        
                    for ofcps_count in range(0, 5):
                        sql_query_ofcps = """
                                            INSERT INTO BIM_OFCPS (
                                                CORP_NO, OFCPS, OFCPS_NM, STATE, REG_DTIME, REG_ID, UPT_DTIME, UPT_ID)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                            """
                        cursor.execute(sql_query_ofcps, [
                            max_num, '100'+str(ofcps_count+1), ofcps_name[ofcps_count], '1', gen1, gen2, upt1, gen2
                        ])
                        
                    for salary_count in range(0, 9):
                        sql_query_salary = """
                                            INSERT INTO BIM_SALARY (
                                                CORP_NO, SALARY_ITEM, SALARY_TYPE, ITEM_NM, TAXT_YN, TRMMG_UNIT, USE_YN, STD_INFO_VAL, REG_DTIME, REG_ID, UPT_DTIME, UPT_ID)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                            """
                        cursor.execute(sql_query_salary, [
                            max_num, empl_salary[salary_count][2], empl_salary[salary_count][3], salary_name[salary_count], empl_salary[salary_count][4], empl_salary[salary_count][5], empl_salary[salary_count][6], empl_salary[salary_count][7],  gen1, gen2, upt1, gen2
                        ])
                        
                    for atend_count in range(0, 10):
                        sql_query_atend = """
                                            INSERT INTO BIM_ATEND (
                                                CORP_NO, LABORTIME_TYPE, LABOR_TIME_NM, ST_TIME, END_TIME, STATE, REG_DTIME, REG_ID, UPT_DTIME, UPT_ID)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                            """
                        cursor.execute(sql_query_atend, [
                            max_num, '000'+str(atend_count+1) , atend_name[atend_count], empl_atend[atend_count][3], empl_atend[atend_count][4], '1', gen1, gen2, upt1, gen2
                        ])

            return Response({"message": "Data inserted successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            logger.error(e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

class CorporationGetInfo(APIView):
    def get(self, request):

        sql_query = """
        SELECT * FROM CMM_CODE WHERE LCODE = '0013' AND SCODE > '0000' AND SCODE < '0010' 
        """         

        # SQL 쿼리 실행
        cursor = connection.cursor()
        cursor.execute(sql_query)

        serialized_corpinfo = []

        for row in cursor.fetchall():
            serialized_corp = {
                "lcode": row[0],
                "scode": row[1],
                "cd_val": row[2],
                "desc": row[3],
                "seq": row[4],
            }
            print(serialized_corp)
            serialized_corpinfo.append(serialized_corp)

        return JsonResponse(serialized_corpinfo, safe=False)
    
class CorporationGetOfcps(APIView):
    def get(self, request):

        sql_query = """
        SELECT * FROM CMM_CODE WHERE LCODE = 0002 AND SCODE > 0001 AND SCODE < 0010
        """         

        # SQL 쿼리 실행
        cursor = connection.cursor()
        cursor.execute(sql_query)

        serialized_corpinfo = []

        for row in cursor.fetchall():
            serialized_corp = {
                "lcode": row[0],
                "scode": row[1],
                "cd_val": row[2],
                "desc": row[3],
                "seq": row[4],
            }
            print(serialized_corp)
            serialized_corpinfo.append(serialized_corp)

        return JsonResponse(serialized_corpinfo, safe=False)