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

class EmployeeAPIView(APIView):
    def get(self, request):
        sql_query = """
        SELECT *
        FROM HRM_EMPL empl
        JOIN HRM_DEPT dept
        ON empl.DEPT_NO = dept.DEPT_NO
        JOIN HRM_SALARY sal
        ON sal.EMPL_NO = empl.EMPL_NO
        ORDER BY CAST(empl.EMPL_NO AS UNSIGNED)
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
                "empl_ssid": row[4], # 주민번호
                "empl_gender": row[5], # 성별
                "empl_telno": row[11], # 전화번호
                "empl_ssid_addr": row[12], # 실거주지
                "empl_rspofc": row[17], # 직책
                "empl_emplym_form": row[18], # 고용형태
                "empl_salary_form": row[19], # 급여형태
                "empl_encpnd": row[20], # 입사일
                "empl_hffc_state": row[21], # 재직상태
                "empl_retire_date": row[22], # 퇴사일자
                "empl_frgnr_yn": row[23], # 외국인여부
                "empl_dept_nm" : row[30], # 부서이름
                "empl_bank" : row[40], # 은행
                "empl_acc" : row[41], # 계좌번호
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)
        
        return JsonResponse(serialized_employees, safe=False)
    
class EmployeeAPIViewSearch(APIView):
    def get(self, request):
        sql_query = """
        SELECT *
        FROM HRM_EMPL empl
        JOIN HRM_DEPT dept
        ON empl.DEPT_NO = dept.DEPT_NO
        JOIN HRM_SALARY sal
        ON sal.EMPL_NO = empl.EMPL_NO
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
                "empl_ssid": row[4], # 주민번호
                "empl_gender": row[5], # 성별
                "empl_telno": row[11], # 전화번호
                "empl_ssid_addr": row[12], # 실거주지
                "empl_rspofc": row[17], # 직책
                "empl_emplym_form": row[18], # 고용형태
                "empl_salary_form": row[19], # 급여형태
                "empl_encpnd": row[20], # 입사일
                "empl_hffc_state": row[21], # 재직상태
                "empl_retire_date": row[22], # 퇴사일자
                "empl_frgnr_yn": row[23], # 외국인여부
                "empl_dept_nm" : row[30], # 부서이름
                "empl_bank" : row[40], # 은행
                "empl_acc" : row[41], # 계좌번호
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)
        
        return JsonResponse(serialized_employees, safe=False)
    
class EmployeeAPIMax(APIView):
    def get(self, request):
        corp_no = '1'
        
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(EMPL_NO)+1 FROM HRM_EMPL WHERE CORP_NO = %s", [corp_no])
        
        serialized_employees = []
        
        for row in cursor.fetchall():
            serialized_empl = {
                "no": row[0],
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)
        
        return JsonResponse(serialized_employees, safe=False)
    
class EmployeeAPIPost(APIView):
    def post(self, request):
        # POST 요청에서 전달된 데이터 가져오기
            data = request.data
            now = datetime.now()
            
            employee_info = data.get('employeeInfo')
            attend_info = data.get('attendInfo')
            salary_info = data.get('salaryInfo')
            frgnr_info = data.get('frgnrInfo')
            
            # HRM_EMPL 테이블
            corp_no_empl = '1' #세션처리예정
            dept_no_empl = '1' #세션처리예정
            empl_nm_empl = employee_info.get('empl_nm')
            ssid_empl = employee_info.get('ssid')
            gender_empl = employee_info.get('gender')
            brthdy_empl = employee_info.get('brthdy')
            lunsolar_empl = employee_info.get('lunsolar')
            mrig_yn_empl = employee_info.get('mrig_yn')
            mrig_anvsry_empl = employee_info.get('mrig_anvsry')
            tel_no_empl = employee_info.get('tel_no')
            mobile_no_empl = employee_info.get('mobile_no')
            ssid_addr_empl = employee_info.get('ssid_addr')
            rlsdnc_addr_empl = employee_info.get('rlsdnc_addr')
            email_empl = employee_info.get('email')
            prsl_email_empl = employee_info.get('prsl_email')
            exctv_yn_empl = employee_info.get('exctv_yn')
            rspofc_empl = employee_info.get('rspofc')
            emplym_form_empl = employee_info.get('emplym_form')
            salary_form_empl = employee_info.get('salary_form')
            encpnd_empl = employee_info.get('encpnd')
            hffc_state_empl = employee_info.get('hffc_state')
            retire_date_empl = employee_info.get('retire_date')
            frgnr_yn_empl = employee_info.get('frgnr_yn')
            reg_dtime_empl = now.strftime('%Y-%m-%d %H:%M:%S')
            reg_id_empl = '관리자' #세션처리예정
            upt_dtime_empl = now.strftime('%Y-%m-%d %H:%M:%S')
            upt_id_empl = '운영자' #세션처리예정
            
            # HRM_ATEND 테이블
            # empl_no_atend = '1' #필요없음
            corp_no_atend = '1' #세션처리예정
            dept_no_atend = '1' #세션처리예정
            base_attendtime_atend = attend_info.get('base_attendtime')
            base_lvofctime_atend = attend_info.get('base_lvofctime')
            mdwk_workday_atend = attend_info.get('mdwk_workday')
            whday_atend = attend_info.get('whday')
            crtlwh_atend = attend_info.get('crtlwh')
            upt_dtime_atend = now.strftime('%Y-%m-%d %H:%M:%S')
            upt_id_atend = '운영자' #세션처리예정

            # HRM_SALARY 테이블
            # empl_no_salary = '1' #필요없음
            corp_no_salary = '1' #세션처리예정
            dept_no_salary = '1' #세션처리예정
            base_salary_salary = salary_info.get('base_salary')
            trn_bank_salary = salary_info.get('trn_bank')
            acc_no_salary = salary_info.get('acc_no')
            npn_pay_yn_salary = salary_info.get('npn_pay_yn')
            npn_mrmrtn_salary = salary_info.get('npn_mrmrtn')
            hlthins_pay_yn_salary = salary_info.get('hlthins_pay_yn')
            hlthins_mrmrtn_salary = salary_info.get('hlthins_mrmrtn')
            empins_pay_yn_salary = salary_info.get('empins_pay_yn')
            empins_mrmrtn_salary = salary_info.get('empins_mrmrtn')
            upt_dtime_salary = now.strftime('%Y-%m-%d %H:%M:%S')
            upt_id_salary = '운영자' #세션처리예정
            
            # HRM_FRGNR 테이블
            empl_no_frgnr = '1' #세션처리예정
            corp_no_frgnr = '1' #세션처리예정
            dept_no_frgnr = '1' #세션처리예정
            dtrmcexp_date_frgnr = frgnr_info.get('dtrmcexp_date')
            dtrmcexp_icny_frgnr = frgnr_info.get('dtrmcexp_icny')
            dtrmcexp_insrnc_amt_frgnr = frgnr_info.get('dtrmcexp_insrnc_amt')
            remark_frgnr = ''
            upt_dtime_frgnr = now.strftime('%Y-%m-%d %H:%M:%S')
            upt_id_frgnr = '운영자' #세션처리예정
            
            corp_no = 1

            try:
                # 직접 SQL 문 사용하여 데이터베이스에 부서 정보 등록
                with transaction.atomic():
                    with connection.cursor() as cursor:
                        
                        cursor.execute("SELECT MAX(CAST(EMPL_NO AS UNSIGNED)) FROM HRM_EMPL WHERE CORP_NO = %s", [corp_no])
                        max_num = cursor.fetchone()[0]
                        max_value = (int(max_num) if max_num else 0) + 1
                        
                        sql_query = """
                                    INSERT INTO HRM_EMPL (
                                        CORP_NO, DEPT_NO, EMPL_NO, EMPL_NM, SSID, GENDER, BRTHDY, LUNISOLAR, MRIG_YN, MRIG_ANVSRY,
                                        TEL_NO, MOBILE_NO, SSID_ADDR, RLRSDNC_ADDR, EMAIL, PRSL_EMAIL, EXCTV_YN, RSPOFC,
                                        EMPLYM_FORM, SALARY_FORM, ENCPND, HFFC_STATE, RETIRE_DATE, FRGNR_YN, REG_DTIME,
                                        REG_ID, UPT_DTIME, UPT_ID)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                    """
                        cursor.execute(sql_query, [
                            corp_no_empl, dept_no_empl, max_value, empl_nm_empl, ssid_empl, gender_empl, brthdy_empl, lunsolar_empl, mrig_yn_empl, mrig_anvsry_empl,
                            tel_no_empl, mobile_no_empl, ssid_addr_empl, rlsdnc_addr_empl, email_empl, prsl_email_empl, exctv_yn_empl, rspofc_empl,
                            emplym_form_empl, salary_form_empl, encpnd_empl, hffc_state_empl, retire_date_empl, frgnr_yn_empl, reg_dtime_empl,
                            reg_id_empl, upt_dtime_empl, upt_id_empl
                        ])
                        
                        sql_query_atend = """
                                            INSERT INTO HRM_ATEND (
                                                EMPL_NO, CORP_NO, DEPT_NO, BASE_ATENDTIME, BASE_LVOFCTIME, MDWK_WORKDAY, WHDAY, CRTLWH, UPT_DTIME, UPT_ID)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                            """
                        cursor.execute(sql_query_atend, [
                            max_value, corp_no_atend, dept_no_atend, base_attendtime_atend,
                            base_lvofctime_atend, mdwk_workday_atend, whday_atend, crtlwh_atend, upt_dtime_atend, upt_id_atend
                        ])
                        
                        sql_query_salary = """
                                            INSERT INTO HRM_SALARY (
                                                EMPL_NO, CORP_NO, DEPT_NO, BASE_SALARY, TRN_BANK, ACC_NO, NPN_PAY_YN, NPN_MRMRTN, 
                                                HLTHINS_PAY_YN, HLTHINS_MRMRTN, EMPINS_PAY_YN, EMPINS_MRMRTN, UPT_DTIME, UPT_ID)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                            """
                        cursor.execute(sql_query_salary, [
                            max_value, corp_no_salary, dept_no_salary, base_salary_salary, trn_bank_salary, acc_no_salary,
                            npn_pay_yn_salary, npn_mrmrtn_salary, hlthins_pay_yn_salary, hlthins_mrmrtn_salary, empins_pay_yn_salary,
                            empins_mrmrtn_salary, upt_dtime_salary, upt_id_salary
                        ])
                        
                        sql_query_frgnr = """
                                            INSERT INTO HRM_FRGNR (
                                                EMPL_NO, CORP_NO, DEPT_NO, DTRMCEXP_DATE, DTRMCEXP_ICNY, DTRMCEXP_INSRNC_AMT, REMARK, UPT_DTIME, UPT_ID)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                            """
                        cursor.execute(sql_query_frgnr, [
                            max_value, corp_no_frgnr, dept_no_frgnr, dtrmcexp_date_frgnr,
                            dtrmcexp_icny_frgnr, dtrmcexp_insrnc_amt_frgnr, remark_frgnr, upt_dtime_frgnr, upt_id_frgnr
                        ])

                return Response({"message": "Data inserted successfully"}, status=status.HTTP_201_CREATED)

            except Exception as e:
                logger.error(e)
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
class EmployeeAPIFmly(APIView):
    def post(self, request):
        
        data_array = request.data
        now = datetime.now()
        
        for data in data_array:
            # HRM_FMLY 테이블
            empl_no_fmly = '1' #세션처리예정
            corp_no_fmly = '1' #세션처리예정
            dept_no_fmly = '1' #세션처리예정
            fmly_no_fmly = '1' #세션처리예정
            constnt_type_fmly = data.get('constnt_type')
            reltn_fmly = data.get('reltn')
            constnt_nm_fmly = data.get('constnt_nm')
            brthdy_fmly = now.strftime('%Y-%m-%d %H:%M:%S')
            livtgt_yn_fmly = data.get('livtgt_yn')
            dednhope_yn_fmly = data.get('dednhope_yn')
            dspsn_yn_fmly = data.get('dspsn_yn')
            state_fmly = 'Y'
            remark_fmly = ''
            reg_dtime_fmly = now.strftime('%Y-%m-%d %H:%M:%S')
            reg_id_fmly = '관리자'
            upt_dtime_fmly = now.strftime('%Y-%m-%d %H:%M:%S')
            upt_id_fmly = '운영자'

            try:
                # 직접 SQL 문 사용하여 데이터베이스에 부서 정보 등록
                with transaction.atomic():
                    with connection.cursor() as cursor:
                        
                        empl_no = '1' # 나중에 바꿔야함 테스트용
                            
                        cursor.execute("SELECT MAX(FMLY_NO) FROM HRM_FMLY WHERE EMPL_NO = %s", [empl_no])
                        max_num = cursor.fetchone()[0]
                        max_value = (int(max_num) if max_num else 0) + 1
                            
                        sql_query_frgnr = """
                                            INSERT INTO HRM_FMLY (
                                                EMPL_NO, CORP_NO, DEPT_NO, FMLY_NO, CONSTNT_TYPE, RELTN, CONSTNT_NM, BRTHDY, LIVTGT_YN, DEDNHOPE_YN, DSPSN_YN, STATE, REMARK, REG_DTIME, REG_ID, UPT_DTIME, UPT_ID)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                        """
                        cursor.execute(sql_query_frgnr, [
                            empl_no_fmly, corp_no_fmly, dept_no_fmly, max_value,
                            constnt_type_fmly, reltn_fmly, constnt_nm_fmly, brthdy_fmly, livtgt_yn_fmly,
                            dednhope_yn_fmly, dspsn_yn_fmly, state_fmly, remark_fmly, reg_dtime_fmly,
                            reg_id_fmly, upt_dtime_fmly, upt_id_fmly
                        ])

            except Exception as e:
                logger.error(e)
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({"message": "Data inserted successfully"}, status=status.HTTP_201_CREATED)
    
class EmployeeAPIRate(APIView):
    def get(self, request):

        cursor = connection.cursor()
        cursor.execute("SELECT LCODE_NM FROM CMM_LCODE WHERE LCODE LIKE 'B%'")
        
        serialized_employees = []
        
        for row in cursor.fetchall():
            serialized_empl = {
                "lcode_nm": row[0],
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)
        
        return JsonResponse(serialized_employees, safe=False)
    
class EmployeeAPIRole(APIView):
    def get(self, request):

        cursor = connection.cursor()
        cursor.execute("SELECT LCODE, LCODE_NM FROM CMM_LCODE WHERE LCODE LIKE 'A%'")
        
        serialized_employees = []
        
        for row in cursor.fetchall():
            serialized_empl = {
                "lcode": row[0],
                "lcode_nm": row[1],
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)
        
        return JsonResponse(serialized_employees, safe=False)
    
class EmployeeAPIDetailTable(APIView):
    def get(self, request):
        # cursor.execute("SELECT MAX(DEPT_NO) FROM HRM_DEPT WHERE CORP_NO = %s", [corp_no])
        empl_id_detail = request.GET.get('empl_id_detail', None)

        cursor = connection.cursor()
        cursor.execute("SELECT LCODE, LCODE_NM FROM CMM_LCODE WHERE LCODE LIKE 'A%'")
        
        serialized_employees = []
        
        for row in cursor.fetchall():
            serialized_empl = {
                "lcode": row[0],
                "lcode_nm": row[1],
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)
        
        return JsonResponse(serialized_employees, safe=False)
    
class EmployeeAPIDetailTableFmly(APIView):
    def get(self, request):
        
        empl_id_detail = request.GET.get('empl_id_detail', None)

        cursor = connection.cursor()
        cursor.execute("SELECT LCODE, LCODE_NM FROM CMM_LCODE WHERE LCODE LIKE 'A%'")
        
        serialized_employees = []
        
        for row in cursor.fetchall():
            serialized_empl = {
                "lcode": row[0],
                "lcode_nm": row[1],
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)
        
        return JsonResponse(serialized_employees, safe=False)