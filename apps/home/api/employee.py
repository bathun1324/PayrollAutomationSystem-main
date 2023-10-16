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
        JOIN BIM_DEPT dept
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
                "no": row[0],  # 회사번호
                "id": row[1],  # 부서번호
                "empl_no": row[2],  # 사원번호
                "empl_rspofc": row[3],  # 직위
                "empl_nm": row[4],  # 사원명
                "empl_gender": row[5],  # 성별
                "empl_reg_dtime": row[6],
                "empl_mrig_yn": row[7],  # 결혼여부
                "empl_prsl_email": row[8],  # 개인이메일
                "empl_brthdy": row[9],  # 생년월일
                "empl_hffc_state": row[10],  # 재직상태
                "empl_exctv_yn": row[11],  # 임원여부
                "empl_photoid": row[12],  # 사진
                "empl_reg_id": row[13],  # 등록자
                "empl_frgnr_yn": row[14],  # 외국인여부
                "empl_telno": row[15],  # 전화번호
                "empl_mobile_no": row[16],  # 휴대폰번호
                "empl_lunisolar": row[17],  # 양음력
                "empl_retire_date": row[18],  # 퇴사일자
                "empl_upt_id": row[19],  # 수정자
                "empl_salary_form": row[20],  # 급여형태
                "empl_ssid": row[21],  # 주민번호
                "empl_email": row[22],  # 이메일
                "empl_emplyn_form": row[23],  # 고용형태
                "empl_mrig_anvsry": row[24],  # 결혼기념일
                "empl_ssid_addr": row[26],  # 주민등록번황 거주지
                "empl_rlsdnc_addr": row[27],  # 실거주지
                "empl_encpnd": row[28],  # 입사일
                "empl_dept_nm": row[31],  # 부서이름
                "empl_bank": row[41],  # 은행
                "empl_acc": row[42],  # 계좌번호
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)


class EmployeeAPIViewSearch(APIView):
    def get(self, request):

        empl_dept_nm = request.GET.get('department', None)
        empl_nm = request.GET.get('employeeName', None)
        empl_frgnr_yn = request.GET.get('foreigner', None)
        empl_emplym_form = request.GET.get('employmentType', None)
        empl_hffc_state = request.GET.get('employmentStatus', None)

        sql_query = """
        SELECT *
        FROM HRM_EMPL empl
        JOIN BIM_DEPT dept
        ON empl.DEPT_NO = dept.DEPT_NO
        JOIN HRM_SALARY sal
        ON sal.EMPL_NO = empl.EMPL_NO
        WHERE 1=1
        """

        values = []

        if empl_dept_nm and empl_dept_nm != 'undefined':
            sql_query += " AND dept.DEPT_NM = %s "
            values.append(empl_dept_nm)

        if empl_nm and empl_nm != 'undefined':
            sql_query += " AND empl.EMPL_NM = %s "
            values.append(empl_nm)

        if empl_frgnr_yn and empl_frgnr_yn != 'undefined':
            sql_query += " AND empl.FRGNR_YN = %s "
            values.append(empl_frgnr_yn)

        if empl_emplym_form and empl_emplym_form != 'undefined':
            sql_query += " AND empl.EMPLYM_FORM = %s "
            values.append(empl_emplym_form)

        if empl_hffc_state and empl_hffc_state != 'undefined':
            sql_query += " AND empl.HFFC_STATE = %s "
            values.append(empl_hffc_state)

        # SQL 쿼리 실행
        cursor = connection.cursor()
        cursor.execute(sql_query, values)

        serialized_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "no": row['CORP_NO'],  # 회사번호
                "id": row['DEPT_NO'],  # 부서번호
                "empl_no": row['EMPL_NO'],  # 사원번호
                "empl_ofcps": row['OFCPS'],  # 직위
                "empl_nm": row['EMPL_NM'],  # 사원명
                "empl_gender": row['GENDER'],  # 성별
                "empl_reg_dtime": row['REG_DTIME'],
                "empl_mrig_yn": row['MRIG_YN'],  # 결혼여부
                "empl_prsl_email": row['PRSL_EMAIL'],  # 개인이메일
                "empl_brthdy": row['BRTHDY'],  # 생년월일
                "empl_hffcstate": row['HFFC_STATE'],  # 재직상태
                "empl_exctv_yn": row['EXCTV_YN'],  # 임원여부
                "empl_photoid": row['PHOTO_ID'],  # 사진
                "empl_reg_id": row['REG_ID'],  # 등록자
                "empl_frgnr_yn": row['FRGNR_YN'],  # 외국인여부
                "empl_tel_no": row['TEL_NO'],  # 전화번호
                "empl_mobile_no": row['MOBILE_NO'],  # 휴대폰번호
                "empl_lunisolar": row['LUNISOLAR'],  # 양음력
                "empl_retire_date": row['RETIRE_DATE'],  # 퇴사일자
                "empl_upt_id": row['UPT_ID'],  # 수정자
                "empl_salary_form": row['SALARY_FORM'],  # 급여형태
                "empl_ssid": row['SSID'],  # 주민번호
                "empl_email": row['EMAIL'],  # 이메일
                "empl_emplyn_form": row['EMPLYN_FORM'],  # 고용형태
                "empl_mrig_anvsry": row['MRIG_ANVSRY'],  # 결혼기념일
                "empl_ssid_addr": row['SSID_ADDR'],  # 주민등록번황 거주지
                "empl_rlsdnc_addr": row['RLRSDNC_ADDR'],  # 실거주지
                "empl_encpnd": row['ENCPND'],  # 입사일
                "empl_dept_nm": row['DEPT_NM'],  # 부서이름
                "empl_bank": row['TRN_BANK'],  # 은행
                "empl_acc": row['ACC_NO'],  # 계좌번호
                "empl_emplym_form": row['EMPLYM_FORM'],  # 고용형태
                "empl_salary_form": row['SALARY_FORM'],  # 급여형태

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

        print(employee_info)

        # HRM_EMPL 테이블
        corp_no_empl = '1'  # 세션처리예정
        dept_no_empl = employee_info.get('dept_no')
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
        reg_id_empl = '관리자'  # 세션처리예정
        upt_dtime_empl = now.strftime('%Y-%m-%d %H:%M:%S')
        upt_id_empl = '운영자'  # 세션처리예정

        # HRM_ATEND 테이블
        # empl_no_atend = '1' #필요없음
        corp_no_atend = '1'  # 세션처리예정
        dept_no_atend = employee_info.get('dept_no')  # 세션처리예정
        base_attendtime_atend = attend_info.get('base_attendtime')
        base_lvofctime_atend = attend_info.get('base_lvofctime')
        mdwk_workday_atend = attend_info.get('mdwk_workday')
        whday_atend = attend_info.get('whday')
        crtlwh_atend = attend_info.get('crtlwh')
        upt_dtime_atend = now.strftime('%Y-%m-%d %H:%M:%S')
        upt_id_atend = '운영자'  # 세션처리예정

        # HRM_SALARY 테이블
        # empl_no_salary = '1' #필요없음
        corp_no_salary = '1'  # 세션처리예정
        dept_no_salary = employee_info.get('dept_no')  # 세션처리예정
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
        upt_id_salary = '운영자'  # 세션처리예정

        # HRM_FRGNR 테이블
        empl_no_frgnr = '1'  # 세션처리예정
        corp_no_frgnr = '1'  # 세션처리예정
        dept_no_frgnr = employee_info.get('dept_no')  # 세션처리예정
        dtrmcexp_date_frgnr = frgnr_info.get('dtrmcexp_date')
        dtrmcexp_icny_frgnr = frgnr_info.get('dtrmcexp_icny')
        dtrmcexp_insrnc_amt_frgnr = frgnr_info.get('dtrmcexp_insrnc_amt')
        remark_frgnr = ''
        upt_dtime_frgnr = now.strftime('%Y-%m-%d %H:%M:%S')
        upt_id_frgnr = '운영자'  # 세션처리예정

        corp_no = 1

        try:
            # 직접 SQL 문 사용하여 데이터베이스에 부서 정보 등록
            with transaction.atomic():
                with connection.cursor() as cursor:

                    cursor.execute(
                        "SELECT MAX(CAST(EMPL_NO AS UNSIGNED)) FROM HRM_EMPL WHERE CORP_NO = %s", [corp_no])
                    max_num = cursor.fetchone()[0]
                    max_value = (int(max_num) if max_num else 0) + 1

                    sql_query = """
                                    INSERT INTO HRM_EMPL (
                                        CORP_NO, DEPT_NO, EMPL_NO, EMPL_NM, SSID, GENDER, BRTHDY, LUNISOLAR, MRIG_YN, MRIG_ANVSRY,
                                        TEL_NO, MOBILE_NO, SSID_ADDR, RLRSDNC_ADDR, EMAIL, PRSL_EMAIL, EXCTV_YN, OFCPS,
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
                                                HLTHINS_PAY_YN, HLTHINS_MRMRTN, EMPINS_PAY_YN, UPT_DTIME, UPT_ID)
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
            empl_no_fmly = '1'  # 세션처리예정
            corp_no_fmly = '1'  # 세션처리예정
            dept_no_fmly = '1'  # 세션처리예정
            fmly_no_fmly = '1'  # 세션처리예정
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

                        empl_no = '1'  # 나중에 바꿔야함 테스트용

                        cursor.execute(
                            "SELECT MAX(FMLY_NO) FROM HRM_FMLY WHERE EMPL_NO = %s", [empl_no])
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
        cursor.execute("SELECT CD_VAL FROM CMM_CODE WHERE LCODE LIKE 'B%'")

        serialized_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "CD_VAL": row[0],
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)


class EmployeeAPIRole(APIView):
    def get(self, request):

        cursor = connection.cursor()
        cursor.execute(
            "SELECT LCODE, CD_VAL FROM CMM_CODE WHERE LCODE LIKE 'A%'")

        serialized_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "lcode": row[0],
                "CD_VAL": row[1],
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)


class EmployeeAPIDetailTable(APIView):
    def get(self, request):

        empl_id_detail = request.GET.get('empl_id_detail', None)

        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM HRM_EMPL empl JOIN BIM_DEPT dept ON empl.DEPT_NO = dept.DEPT_NO JOIN HRM_ATEND atend ON empl.EMPL_NO = atend.EMPL_NO JOIN HRM_FRGNR frgnr ON empl.EMPL_NO = frgnr.EMPL_NO WHERE empl.EMPL_NO = %s", [empl_id_detail])

        serialized_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "dept_no": row[1],  # 부서번호
                "empl_no": row[2],  # 사원번호
                "empl_nm": row[4],  # 사원명
                "ssid": row[21],    # 주민등록번호
                "gender": row[5],   # 성별
                "brthdy": row[9],   # 생년월일
                "lunisolar": row[17],  # 양/음력(양/음)
                "mrig_yn": row[7],  # 결혼여부
                "mrig_anvsry": row[24],  # 결혼기념일
                "tel_no": row[15],  # 전화번호
                "mobile_no": row[16],   # 휴대폰번호
                "ssid_addr": row[26],   # 주민등록번호 주소
                "rlrsdnc_addr": row[27],  # 실거주 주소
                "email": row[22],   # 이메일
                "prsl_email": row[8],  # 개인이메일
                "exctv_yn": row[11],    # 임원여부
                "rspofc": row[3],  # 직위
                "emplym_form": row[23],  # 고용형태
                "salary_form": row[20],  # 급여형태
                "encpnd": row[28],  # 입사일자
                "hffc_state": row[10],  # 재직상태
                "retire_date": row[18],  # 퇴사일자
                "frgnr_yn": row[14],    # 외국인여부(O,X)
                "dtrmcexp_icny": row[51],    # 출국만기보험사
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)


class EmployeeAPIDetailAttend(APIView):
    def get(self, request):

        empl_id_detail = request.GET.get('empl_id_detail', None)

        cursor = connection.cursor()
        cursor.execute(
            " SELECT * FROM HRM_ATEND WHERE EMPL_NO = %s", [empl_id_detail])

        serialized_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "epml_no": row[0],  # 사원번호
                "corp_no": row[1],  # 회사번호
                "dept_no": row[2],  # 부서번호
                "base_attendtime": row[3],  # 기본 출근시간
                "base_lvofctime": row[4],   # 기본 퇴근시간
                "mdwk_workday": row[5],     # 주중 근무일
                "whday": row[6],    # 주휴일
                "crtlwh": row[7],   # 소정근로시간
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)


class EmployeeAPIDetailSalary(APIView):
    def get(self, request):

        empl_id_detail = request.GET.get('empl_id_detail', None)

        cursor = connection.cursor()
        cursor.execute(
            " SELECT * FROM HRM_SALARY WHERE EMPL_NO = %s", [empl_id_detail])

        serialized_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "epml_no": row[0],  # 사원번호
                "corp_no": row[1],  # 회사번호
                "dept_no": row[2],  # 부서번호
                "base_salary": row[3],  # 기본급여
                "trn_bank": row[4],  # 이체은행
                "acc_no": row[5],   # 계좌번호
                "npn_pay_yn": row[6],   # 국민연금납부여부(O/X)
                "npn_mrmrtn": row[7],   # 국민연금월보수액
                "hlthins_pay_yn": row[8],   # 건강보험납부여부(O/X)
                "hlthins_mrmrtn": row[9],   # 건강보험월보수액
                "empins_pay_yn": row[10],   # 고용보험납부여부(O/X)
                "rperins_pay_yn": row[11],  # 요양보험납부여부(O/X)
                "wthtx_taxrt": row[12],  # 원천징수세율
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)


class EmployeeAPIDetailFrgnr(APIView):
    def get(self, request):

        empl_id_detail = request.GET.get('empl_id_detail', None)

        cursor = connection.cursor()
        cursor.execute(
            " SELECT * FROM HRM_FRGNR WHERE EMPL_NO = %s", [empl_id_detail])

        serialized_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "epml_no": row[0],  # 사원번호
                "corp_no": row[1],  # 회사번호
                "dept_no": row[2],  # 부서번호
                "dtrmcexp_date": row[3],    # 출국만기일
                "dtrmcexp_icny": row[4],    # 출국만기보험사(O/X)
                "dtrmcexp_insrnc_amt": row[5],  # 출국만기보험금액
                "remark": row[6],   # 비고
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)


class EmployeeAPIDetailTableFmly(APIView):
    def get(self, request):

        empl_id_detail = request.GET.get('empl_id_detail', None)

        cursor = connection.cursor()
        cursor.execute(
            "SELECT LCODE, CD_VAL FROM CMM_CODE WHERE LCODE LIKE 'A%'")

        serialized_employees = []

        for row in cursor.fetchall():
            serialized_empl = {
                "lcode": row[0],
                "CD_VAL": row[1],
            }
            print(serialized_empl)
            serialized_employees.append(serialized_empl)

        return JsonResponse(serialized_employees, safe=False)


class EmployeeupdateAPIPost(APIView):
    def post(self, request):
        # POST 요청에서 전달된 데이터 가져오기
        data = request.data
        now = datetime.now()

        employee_info = data.get('employeeInfo')
        attend_info = data.get('attendInfo')
        salary_info = data.get('salaryInfo')
        frgnr_info = data.get('frgnrInfo')

        print(employee_info)

        # HRM_EMPL 테이블
        corp_no_empl = '1'  # 세션처리예정
        dept_no_empl = employee_info.get('dept_no')
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
        reg_id_empl = '관리자'  # 세션처리예정
        upt_dtime_empl = now.strftime('%Y-%m-%d %H:%M:%S')
        upt_id_empl = '운영자'  # 세션처리예정

        # HRM_ATEND 테이블
        # empl_no_atend = '1' #필요없음
        corp_no_atend = '1'  # 세션처리예정
        dept_no_atend = employee_info.get('dept_no')  # 세션처리예정
        base_attendtime_atend = attend_info.get('base_attendtime')
        base_lvofctime_atend = attend_info.get('base_lvofctime')
        mdwk_workday_atend = attend_info.get('mdwk_workday')
        whday_atend = attend_info.get('whday')
        crtlwh_atend = attend_info.get('crtlwh')
        upt_dtime_atend = now.strftime('%Y-%m-%d %H:%M:%S')
        upt_id_atend = '운영자'  # 세션처리예정

        # HRM_SALARY 테이블
        # empl_no_salary = '1' #필요없음
        corp_no_salary = '1'  # 세션처리예정
        dept_no_salary = employee_info.get('dept_no')  # 세션처리예정
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
        upt_id_salary = '운영자'  # 세션처리예정

        # HRM_FRGNR 테이블
        empl_no_frgnr = '1'  # 세션처리예정
        corp_no_frgnr = '1'  # 세션처리예정
        dept_no_frgnr = employee_info.get('dept_no')  # 세션처리예정
        dtrmcexp_date_frgnr = frgnr_info.get('dtrmcexp_date')
        dtrmcexp_icny_frgnr = frgnr_info.get('dtrmcexp_icny')
        dtrmcexp_insrnc_amt_frgnr = frgnr_info.get('dtrmcexp_insrnc_amt')
        remark_frgnr = ''
        upt_dtime_frgnr = now.strftime('%Y-%m-%d %H:%M:%S')
        upt_id_frgnr = '운영자'  # 세션처리예정

        corp_no = 1
        empl_no = employee_info.get('empl_no')  # 사원번호
        try:
            # 직접 SQL 문 사용하여 데이터베이스에 부서 정보 수정
            with transaction.atomic():
                with connection.cursor() as cursor:
                    # 외래키 제약조건 비활성화
                    cursor.execute("SET FOREIGN_KEY_CHECKS=0")

                    sql_query = """
                                    UPDATE HRM_EMPL 
                                    SET CORP_NO = %s, DEPT_NO = %s, EMPL_NM = %s, SSID = %s, GENDER = %s, BRTHDY = %s, LUNISOLAR = %s, MRIG_YN = %s, MRIG_ANVSRY = %s,
                                        TEL_NO = %s, MOBILE_NO = %s, SSID_ADDR = %s, RLRSDNC_ADDR = %s, EMAIL = %s, PRSL_EMAIL = %s, EXCTV_YN = %s, RSPOFC = %s,
                                        EMPLYM_FORM = %s, SALARY_FORM = %s, ENCPND = %s, HFFC_STATE = %s, RETIRE_DATE = %s, FRGNR_YN = %s, REG_DTIME = %s,
                                        REG_ID = %s, UPT_DTIME = %s, UPT_ID = %s 
                                    WHERE EMPL_NO = %s
                                    """
                    cursor.execute(sql_query, [
                        corp_no_empl, dept_no_empl, empl_nm_empl, ssid_empl, gender_empl, brthdy_empl, lunsolar_empl, mrig_yn_empl, mrig_anvsry_empl,
                        tel_no_empl, mobile_no_empl, ssid_addr_empl, rlsdnc_addr_empl, email_empl, prsl_email_empl, exctv_yn_empl, rspofc_empl,
                        emplym_form_empl, salary_form_empl, encpnd_empl, hffc_state_empl, retire_date_empl, frgnr_yn_empl, reg_dtime_empl,
                        reg_id_empl, upt_dtime_empl, upt_id_empl, empl_no
                    ])

                    sql_query_atend = """
                                        UPDATE HRM_ATEND
                                        SET CORP_NO = %s, DEPT_NO = %s, BASE_ATENDTIME = %s, BASE_LVOFCTIME = %s, MDWK_WORKDAY = %s, 
                                            WHDAY = %s, CRTLWH = %s, UPT_DTIME = %s, UPT_ID = %s 
                                        WHERE EMPL_NO = %s
                                        """
                    cursor.execute(sql_query_atend, [
                        corp_no_atend, dept_no_atend, base_attendtime_atend,
                        base_lvofctime_atend, mdwk_workday_atend, whday_atend, crtlwh_atend, upt_dtime_atend, upt_id_atend, empl_no
                    ])

                    sql_query_salary = """
                                            UPDATE HRM_SALARY
                                            SET CORP_NO = %s, DEPT_NO = %s, BASE_SALARY = %s, TRN_BANK = %s, ACC_NO = %s, NPN_PAY_YN = %s, NPN_MRMRTN = %s,
                                                HLTHINS_PAY_YN = %s, HLTHINS_MRMRTN = %s, EMPINS_PAY_YN = %s, EMPINS_MRMRTN = %s, UPT_DTIME = %s, UPT_ID = %s
                                            WHERE EMPL_NO = %s
                                            """
                    cursor.execute(sql_query_salary, [
                        corp_no_salary, dept_no_salary, base_salary_salary, trn_bank_salary, acc_no_salary,
                        npn_pay_yn_salary, npn_mrmrtn_salary, hlthins_pay_yn_salary, hlthins_mrmrtn_salary, empins_pay_yn_salary,
                        empins_mrmrtn_salary, upt_dtime_salary, upt_id_salary, empl_no
                    ])

                    sql_query_frgnr = """
                                            UPDATE HRM_FRGNR
                                            SET CORP_NO = %s, DEPT_NO = %s, DTRMCEXP_DATE = %s, DTRMCEXP_ICNY = %s, 
                                                DTRMCEXP_INSRNC_AMT = %s, REMARK = %s, UPT_DTIME = %s, UPT_ID = %s
                                            WHERE EMPL_NO = %s
                                            """
                    cursor.execute(sql_query_frgnr, [
                        corp_no_frgnr, dept_no_frgnr, dtrmcexp_date_frgnr,
                        dtrmcexp_icny_frgnr, dtrmcexp_insrnc_amt_frgnr, remark_frgnr, upt_dtime_frgnr, upt_id_frgnr, empl_no
                    ])
                    # 외래키 제약조건 활성화
                    cursor.execute("SET FOREIGN_KEY_CHECKS=1")

            return Response({"message": "Data updated successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            logger.error(e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
