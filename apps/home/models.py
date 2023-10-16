# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AtmBsrp(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    empl_no = models.CharField(db_column='EMPL_NO', max_length=50)
    # Field name made lowercase.
    req_dtime = models.DateTimeField(db_column='REQ_DTIME')
    # Field name made lowercase.
    aprv_state = models.CharField(
        db_column='APRV_STATE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    btrar = models.CharField(
        db_column='BTRAR', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    bsrp_goal = models.CharField(
        db_column='BSRP_GOAL', max_length=1000, blank=True, null=True)
    # Field name made lowercase.
    bsrp_conts = models.CharField(
        db_column='BSRP_CONTS', max_length=4000, blank=True, null=True)
    # Field name made lowercase.
    bsrp_nmpr = models.IntegerField(
        db_column='BSRP_NMPR', blank=True, null=True)
    # Field name made lowercase.
    st_date = models.DateField(db_column='ST_DATE', blank=True, null=True)
    # Field name made lowercase.
    end_date = models.DateField(db_column='END_DATE', blank=True, null=True)
    # Field name made lowercase.
    expect_btrps = models.DecimalField(
        db_column='EXPECT_BTRPS', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    prepay_amt = models.DecimalField(
        db_column='PREPAY_AMT', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    btrps_stl_yn = models.CharField(
        db_column='BTRPS_STL_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    btrps_tamt = models.DecimalField(
        db_column='BTRPS_TAMT', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ATM_BSRP'
        unique_together = (('corp_no', 'dept_no', 'empl_no', 'req_dtime'),)


class AtmCmtng(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    empl_no = models.CharField(db_column='EMPL_NO', max_length=50)
    # Field name made lowercase.
    cmtng_dtime = models.DateTimeField(db_column='CMTNG_DTIME')
    # Field name made lowercase.
    cmtng_type = models.CharField(
        db_column='CMTNG_TYPE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    applc_yn = models.CharField(
        db_column='APPLC_YN', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ATM_CMTNG'
        unique_together = (('corp_no', 'dept_no', 'empl_no', 'cmtng_dtime'),)


class AtmDaly(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    empl_no = models.CharField(db_column='EMPL_NO', max_length=50)
    # Field name made lowercase.
    work_date = models.DateField(db_column='WORK_DATE')
    # Field name made lowercase.
    work_sch = models.CharField(
        db_column='WORK_SCH', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    atend_time = models.DateTimeField(
        db_column='ATEND_TIME', blank=True, null=True)
    # Field name made lowercase.
    lvofc_time = models.DateTimeField(
        db_column='LVOFC_TIME', blank=True, null=True)
    # Field name made lowercase.
    gnot = models.DateTimeField(db_column='GNOT', blank=True, null=True)
    # Field name made lowercase.
    rtn = models.DateTimeField(db_column='RTN', blank=True, null=True)
    # Field name made lowercase.
    atend_jdgmnt = models.CharField(
        db_column='ATEND_JDGMNT', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    lvofc_jdgmnt = models.CharField(
        db_column='LVOFC_JDGMNT', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    laten_time = models.TimeField(
        db_column='LATEN_TIME', blank=True, null=True)
    # Field name made lowercase.
    gnot_time = models.TimeField(db_column='GNOT_TIME', blank=True, null=True)
    # Field name made lowercase.
    elpd_atend = models.TimeField(
        db_column='ELPD_ATEND', blank=True, null=True)
    # Field name made lowercase.
    extn_work = models.TimeField(db_column='EXTN_WORK', blank=True, null=True)
    # Field name made lowercase.
    night_work = models.TimeField(
        db_column='NIGHT_WORK', blank=True, null=True)
    # Field name made lowercase.
    hday_work = models.TimeField(db_column='HDAY_WORK', blank=True, null=True)
    # Field name made lowercase.
    realwork_time = models.TimeField(
        db_column='REALWORK_TIME', blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ATM_DALY'
        unique_together = (('corp_no', 'dept_no', 'empl_no', 'work_date'),)


class AtmMonthly(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    empl_no = models.CharField(db_column='EMPL_NO', max_length=50)
    # Field name made lowercase.
    work_ymon = models.CharField(db_column='WORK_YMON', max_length=6)
    # Field name made lowercase.
    use_yrvc = models.DecimalField(
        db_column='USE_YRVC', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    laten_time = models.TimeField(
        db_column='LATEN_TIME', blank=True, null=True)
    # Field name made lowercase.
    gnot_time = models.TimeField(db_column='GNOT_TIME', blank=True, null=True)
    # Field name made lowercase.
    whday_time = models.TimeField(
        db_column='WHDAY_TIME', blank=True, null=True)
    # Field name made lowercase.
    extn_work = models.TimeField(db_column='EXTN_WORK', blank=True, null=True)
    # Field name made lowercase.
    night_work = models.TimeField(
        db_column='NIGHT_WORK', blank=True, null=True)
    # Field name made lowercase.
    hday_work = models.TimeField(db_column='HDAY_WORK', blank=True, null=True)
    # Field name made lowercase.
    realwork_time = models.TimeField(
        db_column='REALWORK_TIME', blank=True, null=True)
    # Field name made lowercase.
    paidprc_time = models.TimeField(
        db_column='PAIDPRC_TIME', blank=True, null=True)
    # Field name made lowercase.
    extnlabor_wkday = models.TimeField(
        db_column='EXTNLABOR_WKDAY', blank=True, null=True)
    # Field name made lowercase.
    extnlabor_hday = models.TimeField(
        db_column='EXTNLABOR_HDAY', blank=True, null=True)
    # Field name made lowercase.
    labortime_wkday = models.TimeField(
        db_column='LABORTIME_WKDAY', blank=True, null=True)
    # Field name made lowercase.
    labortime_hday = models.TimeField(
        db_column='LABORTIME_HDAY', blank=True, null=True)
    # Field name made lowercase.
    baselabor_time = models.TimeField(
        db_column='BASELABOR_TIME', blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ATM_MONTHLY'
        unique_together = (('corp_no', 'dept_no', 'empl_no', 'work_ymon'),)


class AtmVcatn(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    empl_no = models.CharField(db_column='EMPL_NO', max_length=50)
    # Field name made lowercase.
    req_dtime = models.DateTimeField(db_column='REQ_DTIME')
    # Field name made lowercase.
    aprv_state = models.CharField(
        db_column='APRV_STATE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    vcatn_type = models.CharField(
        db_column='VCATN_TYPE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    vcatn_kind = models.CharField(
        db_column='VCATN_KIND', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    st_date = models.DateField(db_column='ST_DATE', blank=True, null=True)
    # Field name made lowercase.
    end_date = models.DateField(db_column='END_DATE', blank=True, null=True)
    # Field name made lowercase.
    vcatn_daycnt = models.IntegerField(
        db_column='VCATN_DAYCNT', blank=True, null=True)
    # Field name made lowercase.
    realuse_yn = models.CharField(
        db_column='REALUSE_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    vcatn_resn = models.CharField(
        db_column='VCATN_RESN', max_length=1000, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ATM_VCATN'
        unique_together = (('corp_no', 'dept_no', 'empl_no', 'req_dtime'),)


class AtmYrvcmon(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    empl_no = models.CharField(db_column='EMPL_NO', max_length=50)
    # Field name made lowercase.
    use_year = models.CharField(db_column='USE_YEAR', max_length=4)
    # Field name made lowercase.
    use_ymon = models.CharField(db_column='USE_YMON', max_length=6)
    # Field name made lowercase.
    occur_yrvc = models.DecimalField(
        db_column='OCCUR_YRVC', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    use_yrvc = models.DecimalField(
        db_column='USE_YRVC', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    accml_yrvc = models.DecimalField(
        db_column='ACCML_YRVC', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ATM_YRVCMON'
        unique_together = (
            ('corp_no', 'dept_no', 'empl_no', 'use_year', 'use_ymon'),)


class AtmYrvcyear(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    empl_no = models.CharField(db_column='EMPL_NO', max_length=50)
    # Field name made lowercase.
    use_year = models.CharField(db_column='USE_YEAR', max_length=4)
    # Field name made lowercase.
    eyear_occur = models.DecimalField(
        db_column='EYEAR_OCCUR', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    occuryrvc_sum = models.DecimalField(
        db_column='OCCURYRVC_SUM', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    useyrvc_sum = models.DecimalField(
        db_column='USEYRVC_SUM', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    accmlyrvc_sum = models.DecimalField(
        db_column='ACCMLYRVC_SUM', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    eyear_cyfd_yrvc = models.DecimalField(
        db_column='EYEAR_CYFD_YRVC', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    eyear_cyfd_mtyvc = models.DecimalField(
        db_column='EYEAR_CYFD_MTYVC', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    eyear_cyfd_sum = models.DecimalField(
        db_column='EYEAR_CYFD_SUM', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    thsyr_occuryrvc = models.DecimalField(
        db_column='THSYR_OCCURYRVC', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    thsyr_occurmtyvc = models.DecimalField(
        db_column='THSYR_OCCURMTYVC', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    prvyr_use = models.DecimalField(
        db_column='PRVYR_USE', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    thsyr_use = models.DecimalField(
        db_column='THSYR_USE', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    unuse_exp_yrvc = models.DecimalField(
        db_column='UNUSE_EXP_YRVC', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    unuse_exp_mtyvc = models.DecimalField(
        db_column='UNUSE_EXP_MTYVC', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    unuse_exp_sum = models.DecimalField(
        db_column='UNUSE_EXP_SUM', max_digits=4, decimal_places=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ATM_YRVCYEAR'
        unique_together = (('corp_no', 'dept_no', 'empl_no', 'use_year'),)


class BimAtend(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    labortime_type = models.CharField(db_column='LABORTIME_TYPE', max_length=6)
    # Field name made lowercase.
    labor_time_nm = models.CharField(
        db_column='LABOR_TIME_NM', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    st_time = models.CharField(
        db_column='ST_TIME', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    end_time = models.CharField(
        db_column='END_TIME', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    state = models.CharField(
        db_column='STATE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIM_ATEND'
        unique_together = (('corp_no', 'labortime_type'),)


class BimDept(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    dept_nm = models.CharField(
        db_column='DEPT_NM', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    state = models.CharField(
        db_column='STATE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIM_DEPT'
        unique_together = (('corp_no', 'dept_no'),)


class BimHday(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    std_year = models.CharField(db_column='STD_YEAR', max_length=4)
    # Field name made lowercase.
    hday_date = models.CharField(db_column='HDAY_DATE', max_length=4)
    # Field name made lowercase.
    hday_nm = models.CharField(
        db_column='HDAY_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    type = models.CharField(
        db_column='TYPE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIM_HDAY'
        unique_together = (('corp_no', 'std_year', 'hday_date'),)


class BimOfcps(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    ofcps = models.CharField(db_column='OFCPS', max_length=6)
    # Field name made lowercase.
    ofcps_nm = models.CharField(
        db_column='OFCPS_NM', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    state = models.CharField(
        db_column='STATE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIM_OFCPS'
        unique_together = (('corp_no', 'ofcps'),)


class BimSalary(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    salary_item = models.CharField(db_column='SALARY_ITEM', max_length=6)
    # Field name made lowercase.
    salary_type = models.CharField(db_column='SALARY_TYPE', max_length=1)
    # Field name made lowercase.
    item_nm = models.CharField(
        db_column='ITEM_NM', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    taxt_yn = models.CharField(
        db_column='TAXT_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    trmmg_unit = models.CharField(
        db_column='TRMMG_UNIT', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    use_yn = models.CharField(
        db_column='USE_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    std_info_val = models.CharField(
        db_column='STD_INFO_VAL', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIM_SALARY'
        unique_together = (('corp_no', 'salary_item', 'salary_type'),)


class CmmBoard(models.Model):
    # Field name made lowercase.
    board_no = models.IntegerField(db_column='BOARD_NO', primary_key=True)
    # Field name made lowercase.
    title = models.CharField(
        db_column='TITLE', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    conts = models.CharField(
        db_column='CONTS', max_length=4000, blank=True, null=True)
    # Field name made lowercase.
    rdcnt = models.IntegerField(db_column='RDCNT', blank=True, null=True)
    # Field name made lowercase.
    secret_yn = models.CharField(
        db_column='SECRET_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_BOARD'


class CmmBoardcmnt(models.Model):
    # Field name made lowercase.
    board_no = models.IntegerField(db_column='BOARD_NO', primary_key=True)
    # Field name made lowercase.
    cmnt_no = models.IntegerField(db_column='CMNT_NO')
    # Field name made lowercase.
    conts = models.CharField(
        db_column='CONTS', max_length=4000, blank=True, null=True)
    # Field name made lowercase.
    cmnt_depth = models.IntegerField(
        db_column='CMNT_DEPTH', blank=True, null=True)
    # Field name made lowercase.
    bundle_id = models.IntegerField(
        db_column='BUNDLE_ID', blank=True, null=True)
    # Field name made lowercase.
    bundle_depth = models.IntegerField(
        db_column='BUNDLE_DEPTH', blank=True, null=True)
    # Field name made lowercase.
    secret_yn = models.CharField(
        db_column='SECRET_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    delete_yn = models.CharField(
        db_column='DELETE_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_BOARDCMNT'
        unique_together = (('board_no', 'cmnt_no'),)


class CmmBoardfile(models.Model):
    # Field name made lowercase.
    board_no = models.IntegerField(db_column='BOARD_NO', primary_key=True)
    # Field name made lowercase.
    cmnt_no = models.IntegerField(db_column='CMNT_NO')
    # Field name made lowercase.
    file_no = models.IntegerField(db_column='FILE_NO')
    # Field name made lowercase.
    file_org_nm = models.CharField(
        db_column='FILE_ORG_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    file_modify_nm = models.CharField(
        db_column='FILE_MODIFY_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    file_path = models.CharField(
        db_column='FILE_PATH', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    file_size = models.IntegerField(
        db_column='FILE_SIZE', blank=True, null=True)
    # Field name made lowercase.
    crt_dtime = models.DateTimeField(
        db_column='CRT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_BOARDFILE'
        unique_together = (('board_no', 'cmnt_no', 'file_no'),)


class CmmCntrct(models.Model):
    # Field name made lowercase.
    board_no = models.IntegerField(db_column='BOARD_NO', primary_key=True)
    # Field name made lowercase.
    req_type = models.CharField(
        db_column='REQ_TYPE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    title = models.CharField(
        db_column='TITLE', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    conts = models.CharField(
        db_column='CONTS', max_length=4000, blank=True, null=True)
    # Field name made lowercase.
    progrs_state = models.CharField(
        db_column='PROGRS_STATE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    rdcnt = models.IntegerField(db_column='RDCNT', blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_CNTRCT'


class CmmCntrctcmnt(models.Model):
    # Field name made lowercase.
    board_no = models.IntegerField(db_column='BOARD_NO', primary_key=True)
    # Field name made lowercase.
    cmnt_no = models.IntegerField(db_column='CMNT_NO')
    # Field name made lowercase.
    conts = models.CharField(
        db_column='CONTS', max_length=4000, blank=True, null=True)
    # Field name made lowercase.
    cmnt_depth = models.IntegerField(
        db_column='CMNT_DEPTH', blank=True, null=True)
    # Field name made lowercase.
    bundle_id = models.IntegerField(
        db_column='BUNDLE_ID', blank=True, null=True)
    # Field name made lowercase.
    bundle_depth = models.IntegerField(
        db_column='BUNDLE_DEPTH', blank=True, null=True)
    # Field name made lowercase.
    secret_yn = models.CharField(
        db_column='SECRET_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    delete_yn = models.CharField(
        db_column='DELETE_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_CNTRCTCMNT'
        unique_together = (('board_no', 'cmnt_no'),)


class CmmCode(models.Model):
    # Field name made lowercase.
    lcode = models.CharField(db_column='LCODE', primary_key=True, max_length=4)
    # Field name made lowercase.
    scode = models.CharField(db_column='SCODE', max_length=6)
    # Field name made lowercase.
    cd_val = models.CharField(
        db_column='CD_VAL', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)
    # Field name made lowercase.
    desc = models.CharField(
        db_column='DESC', max_length=4000, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_CODE'
        unique_together = (('lcode', 'scode'),)


class CmmConnlog(models.Model):
    # Field name made lowercase.
    login_id = models.CharField(
        db_column='LOGIN_ID', primary_key=True, max_length=15)
    # Field name made lowercase.
    conn_dtime = models.DateTimeField(db_column='CONN_DTIME')
    # Field name made lowercase.
    acs_ip = models.CharField(
        db_column='ACS_IP', max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_CONNLOG'
        unique_together = (('login_id', 'conn_dtime'),)


class CmmInq(models.Model):
    # Field name made lowercase.
    board_no = models.IntegerField(db_column='BOARD_NO', primary_key=True)
    # Field name made lowercase.
    title = models.CharField(
        db_column='TITLE', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    conts = models.CharField(
        db_column='CONTS', max_length=4000, blank=True, null=True)
    # Field name made lowercase.
    rdcnt = models.IntegerField(db_column='RDCNT', blank=True, null=True)
    # Field name made lowercase.
    secret_yn = models.CharField(
        db_column='SECRET_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_INQ'


class CmmInqcmnt(models.Model):
    # Field name made lowercase.
    board_no = models.IntegerField(db_column='BOARD_NO', primary_key=True)
    # Field name made lowercase.
    cmnt_no = models.IntegerField(db_column='CMNT_NO')
    # Field name made lowercase.
    conts = models.CharField(
        db_column='CONTS', max_length=4000, blank=True, null=True)
    # Field name made lowercase.
    cmnt_depth = models.IntegerField(
        db_column='CMNT_DEPTH', blank=True, null=True)
    # Field name made lowercase.
    bundle_id = models.IntegerField(
        db_column='BUNDLE_ID', blank=True, null=True)
    # Field name made lowercase.
    bundle_depth = models.IntegerField(
        db_column='BUNDLE_DEPTH', blank=True, null=True)
    # Field name made lowercase.
    secret_yn = models.CharField(
        db_column='SECRET_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    delete_yn = models.CharField(
        db_column='DELETE_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_INQCMNT'
        unique_together = (('board_no', 'cmnt_no'),)


class CmmInqfile(models.Model):
    # Field name made lowercase.
    board_no = models.IntegerField(db_column='BOARD_NO', primary_key=True)
    # Field name made lowercase.
    cmnt_no = models.IntegerField(db_column='CMNT_NO')
    # Field name made lowercase.
    file_no = models.IntegerField(db_column='FILE_NO')
    # Field name made lowercase.
    file_org_nm = models.CharField(
        db_column='FILE_ORG_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    file_modify_nm = models.CharField(
        db_column='FILE_MODIFY_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    file_path = models.CharField(
        db_column='FILE_PATH', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    crt_dtime = models.DateTimeField(
        db_column='CRT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    file_size = models.IntegerField(
        db_column='FILE_SIZE', blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_INQFILE'
        unique_together = (('board_no', 'cmnt_no', 'file_no'),)


class CmmLogin(models.Model):
    # Field name made lowercase.
    login_id = models.CharField(
        db_column='LOGIN_ID', primary_key=True, max_length=15)
    # Field name made lowercase.
    login_pwd = models.CharField(
        db_column='LOGIN_PWD', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    perm_id = models.CharField(
        db_column='PERM_ID', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    empl_no = models.CharField(
        db_column='EMPL_NO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', blank=True, null=True)
    # Field name made lowercase.
    dept_no = models.CharField(
        db_column='DEPT_NO', max_length=6, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_LOGIN'


class CmmMunu(models.Model):
    # Field name made lowercase.
    menu_id = models.CharField(
        db_column='MENU_ID', primary_key=True, max_length=4)
    # Field name made lowercase.
    parent_menu_id = models.CharField(
        db_column='PARENT_MENU_ID', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    menu_nm = models.CharField(
        db_column='MENU_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    menu_seq = models.IntegerField(db_column='MENU_SEQ', blank=True, null=True)
    # Field name made lowercase.
    menu_icon = models.IntegerField(
        db_column='MENU_ICON', blank=True, null=True)
    # Field name made lowercase.
    pgm_id = models.CharField(
        db_column='PGM_ID', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    use_yn = models.CharField(
        db_column='USE_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_MUNU'


class CmmMunuperm(models.Model):
    # Field name made lowercase.
    menu_id = models.CharField(
        db_column='MENU_ID', primary_key=True, max_length=4)
    # Field name made lowercase.
    perm_id = models.CharField(db_column='PERM_ID', max_length=4)
    # Field name made lowercase.
    parent_menu_id = models.CharField(
        db_column='PARENT_MENU_ID', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_MUNUPERM'
        unique_together = (('menu_id', 'perm_id'),)


class CmmPerm(models.Model):
    # Field name made lowercase.
    perm_id = models.CharField(
        db_column='PERM_ID', primary_key=True, max_length=4)
    # Field name made lowercase.
    perm_nm = models.CharField(
        db_column='PERM_NM', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    use_yn = models.CharField(
        db_column='USE_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_PERM'


class CmmPgm(models.Model):
    # Field name made lowercase.
    pgm_id = models.CharField(
        db_column='PGM_ID', primary_key=True, max_length=10)
    # Field name made lowercase.
    pgm_nm = models.CharField(
        db_column='PGM_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    pgm_url = models.CharField(
        db_column='PGM_URL', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    pgm_desc = models.CharField(
        db_column='PGM_DESC', max_length=400, blank=True, null=True)
    # Field name made lowercase.
    parent_pgm_id = models.CharField(
        db_column='PARENT_PGM_ID', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    role_type_cd = models.CharField(
        db_column='ROLE_TYPE_CD', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    use_yn = models.CharField(
        db_column='USE_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CMM_PGM'


class ComAtendlst(models.Model):
    # Field name made lowercase.
    grp_no = models.IntegerField(db_column='GRP_NO', primary_key=True)
    # Field name made lowercase.
    lcode = models.CharField(db_column='LCODE', max_length=4)
    # Field name made lowercase.
    scode = models.CharField(db_column='SCODE', max_length=6)
    # Field name made lowercase.
    st_time = models.CharField(
        db_column='ST_TIME', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    end_time = models.CharField(
        db_column='END_TIME', max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_ATENDLST'
        unique_together = (('grp_no', 'lcode', 'scode'),)


class ComCntrct(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    cntrct_form = models.CharField(
        db_column='CNTRCT_FORM', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    state = models.CharField(
        db_column='STATE', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cntrct_date = models.DateField(
        db_column='CNTRCT_DATE', blank=True, null=True)
    # Field name made lowercase.
    exp_date = models.DateField(db_column='EXP_DATE', blank=True, null=True)
    # Field name made lowercase.
    pmt_date = models.DateField(db_column='PMT_DATE', blank=True, null=True)
    # Field name made lowercase.
    ter_date = models.DateField(db_column='TER_DATE', blank=True, null=True)
    # Field name made lowercase.
    mtyvc_stl_std = models.CharField(
        db_column='MTYVC_STL_STD', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    tml_use_yn = models.CharField(
        db_column='TML_USE_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_CNTRCT'


class ComCntrcthis(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    rev_no = models.IntegerField(db_column='REV_NO')
    # Field name made lowercase.
    cntrct_form = models.CharField(
        db_column='CNTRCT_FORM', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    state = models.CharField(
        db_column='STATE', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cntrct_date = models.DateField(
        db_column='CNTRCT_DATE', blank=True, null=True)
    # Field name made lowercase.
    exp_date = models.DateField(db_column='EXP_DATE', blank=True, null=True)
    # Field name made lowercase.
    pmt_date = models.DateField(db_column='PMT_DATE', blank=True, null=True)
    # Field name made lowercase.
    ter_date = models.DateField(db_column='TER_DATE', blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_CNTRCTHIS'
        unique_together = (('corp_no', 'rev_no'),)


class ComCorp(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    corp_nm = models.CharField(
        db_column='CORP_NM', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    repre_nm = models.CharField(
        db_column='REPRE_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    bizm_no = models.CharField(
        db_column='BIZM_NO', max_length=13, blank=True, null=True)
    # Field name made lowercase.
    repre_telno = models.CharField(
        db_column='REPRE_TELNO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    addr = models.CharField(
        db_column='ADDR', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    empl_num = models.IntegerField(db_column='EMPL_NUM', blank=True, null=True)
    # Field name made lowercase.
    mngr_nm = models.CharField(
        db_column='MNGR_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    ofcps = models.CharField(
        db_column='OFCPS', max_length=6, blank=True, null=True)
    # Field name made lowercase.
    corp_telno = models.CharField(
        db_column='CORP_TELNO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='EMAIL', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    mobile_no = models.CharField(
        db_column='MOBILE_NO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    mngr_id = models.CharField(
        db_column='MNGR_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    dept_info = models.IntegerField(
        db_column='DEPT INFO', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    ofcps_info = models.IntegerField(
        db_column='OFCPS INFO', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    atend_info = models.IntegerField(
        db_column='ATEND INFO', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    salary_info = models.IntegerField(
        db_column='SALARY INFO', blank=True, null=True)
    # Field name made lowercase.
    logo_id = models.IntegerField(db_column='LOGO_ID', blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_CORP'


class ComCorphis(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    rev_no = models.IntegerField(db_column='REV_NO')
    # Field name made lowercase.
    corp_nm = models.CharField(
        db_column='CORP_NM', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    repre_nm = models.CharField(
        db_column='REPRE_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    bizm_no = models.CharField(
        db_column='BIZM_NO', max_length=13, blank=True, null=True)
    # Field name made lowercase.
    repre_telno = models.CharField(
        db_column='REPRE_TELNO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    addr = models.CharField(
        db_column='ADDR', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    empl_num = models.IntegerField(db_column='EMPL_NUM', blank=True, null=True)
    # Field name made lowercase.
    mngr_nm = models.CharField(
        db_column='MNGR_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    ofcps = models.CharField(
        db_column='OFCPS', max_length=6, blank=True, null=True)
    # Field name made lowercase.
    corp_telno = models.CharField(
        db_column='CORP_TELNO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='EMAIL', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    mobile_no = models.CharField(
        db_column='MOBILE_NO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    mngr_id = models.CharField(
        db_column='MNGR_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    dept_info = models.IntegerField(
        db_column='DEPT_INFO', blank=True, null=True)
    # Field name made lowercase.
    grp_no = models.IntegerField(db_column='GRP_NO', blank=True, null=True)
    # Field name made lowercase.
    atend_info = models.IntegerField(
        db_column='ATEND_INFO', blank=True, null=True)
    # Field name made lowercase.
    salary_info = models.IntegerField(
        db_column='SALARY_INFO', blank=True, null=True)
    # Field name made lowercase.
    logo_id = models.IntegerField(db_column='LOGO_ID', blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_CORPHIS'
        unique_together = (('corp_no', 'rev_no'),)


class ComCorplogo(models.Model):
    # Field name made lowercase.
    logo_id = models.IntegerField(db_column='LOGO_ID', primary_key=True)
    # Field name made lowercase.
    file_org_nm = models.CharField(
        db_column='FILE_ORG_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    file_modify_nm = models.CharField(
        db_column='FILE_MODIFY_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    file_path = models.CharField(
        db_column='FILE_PATH', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    file_size = models.IntegerField(
        db_column='FILE_SIZE', blank=True, null=True)
    # Field name made lowercase.
    crt_dtime = models.DateTimeField(
        db_column='CRT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_CORPLOGO'


class ComGrpinfo(models.Model):
    # Field name made lowercase.
    grp_no = models.IntegerField(db_column='GRP_NO', primary_key=True)
    # Field name made lowercase.
    grp_type = models.CharField(
        db_column='GRP_TYPE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    grp_nm = models.CharField(
        db_column='GRP_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    state = models.CharField(
        db_column='STATE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_GRPINFO'


class ComHday(models.Model):
    # Field name made lowercase.
    std_year = models.CharField(
        db_column='STD_YEAR', primary_key=True, max_length=4)
    # Field name made lowercase.
    hday_date = models.CharField(db_column='HDAY_DATE', max_length=4)
    # Field name made lowercase.
    hday_nm = models.CharField(
        db_column='HDAY_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    type = models.CharField(
        db_column='TYPE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    applc_dtime = models.DateTimeField(
        db_column='APPLC_DTIME', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_HDAY'
        unique_together = (('std_year', 'hday_date'),)


class ComIcmtaxrt(models.Model):
    # Field name made lowercase.
    std_year = models.CharField(
        db_column='STD_YEAR', primary_key=True, max_length=4)
    # Field name made lowercase.
    taxt_std_lwlt = models.DecimalField(
        db_column='TAXT_STD_LWLT', max_digits=13, decimal_places=0)
    # Field name made lowercase.
    taxt_std_uplt = models.DecimalField(
        db_column='TAXT_STD_UPLT', max_digits=13, decimal_places=0)
    # Field name made lowercase.
    taxrt = models.DecimalField(
        db_column='TAXRT', max_digits=5, decimal_places=3, blank=True, null=True)
    # Field name made lowercase.
    dedn_amt = models.DecimalField(
        db_column='DEDN_AMT', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    applc_dtime = models.DateTimeField(
        db_column='APPLC_DTIME', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_ICMTAXRT'
        unique_together = (('std_year', 'taxt_std_lwlt', 'taxt_std_uplt'),)


class ComInsrncrate(models.Model):
    # Field name made lowercase.
    std_date = models.DateField(db_column='STD_DATE', primary_key=True)
    # Field name made lowercase.
    irncf_type = models.CharField(db_column='IRNCF_TYPE', max_length=2)
    # Field name made lowercase.
    insrnc_rate = models.DecimalField(
        db_column='INSRNC_RATE', max_digits=5, decimal_places=3, blank=True, null=True)
    # Field name made lowercase.
    lwstlmt_amt = models.DecimalField(
        db_column='LWSTLMT_AMT', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    toplmt_amt = models.DecimalField(
        db_column='TOPLMT_AMT', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    state = models.CharField(
        db_column='STATE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    applc_dtime = models.DateTimeField(
        db_column='APPLC_DTIME', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_INSRNCRATE'
        unique_together = (('std_date', 'irncf_type'),)


class ComOgdplst(models.Model):
    # Field name made lowercase.
    grp_no = models.IntegerField(db_column='GRP_NO', primary_key=True)
    # Field name made lowercase.
    lcode = models.CharField(db_column='LCODE', max_length=4)
    # Field name made lowercase.
    scode = models.CharField(db_column='SCODE', max_length=6)

    class Meta:
        managed = False
        db_table = 'COM_OGDPLST'
        unique_together = (('grp_no', 'lcode', 'scode'),)


class ComSalarylst(models.Model):
    # Field name made lowercase.
    grp_no = models.IntegerField(db_column='GRP_NO', primary_key=True)
    # Field name made lowercase.
    lcode = models.CharField(db_column='LCODE', max_length=4)
    # Field name made lowercase.
    scode = models.CharField(db_column='SCODE', max_length=6)
    # Field name made lowercase.
    salary_type = models.CharField(
        db_column='SALARY_TYPE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    item_nm = models.CharField(
        db_column='ITEM_NM', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    taxt_yn = models.CharField(
        db_column='TAXT_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    trmmg_unit = models.CharField(
        db_column='TRMMG_UNIT', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    use_yn = models.CharField(
        db_column='USE_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    std_info_val = models.CharField(
        db_column='STD_INFO_VAL', max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_SALARYLST'
        unique_together = (('grp_no', 'lcode', 'scode'),)


class ComSmpltax(models.Model):
    # Field name made lowercase.
    std_year = models.CharField(
        db_column='STD_YEAR', primary_key=True, max_length=4)
    # Field name made lowercase.
    salary_above = models.DecimalField(
        db_column='SALARY_ABOVE', max_digits=13, decimal_places=0)
    # Field name made lowercase.
    salary_belo = models.DecimalField(
        db_column='SALARY_BELO', max_digits=13, decimal_places=0)
    # Field name made lowercase.
    fmly_num_1 = models.IntegerField(
        db_column='FMLY_NUM_1', blank=True, null=True)
    # Field name made lowercase.
    fmly_num_2 = models.IntegerField(
        db_column='FMLY_NUM_2', blank=True, null=True)
    # Field name made lowercase.
    fmly_num_3 = models.IntegerField(
        db_column='FMLY_NUM_3', blank=True, null=True)
    # Field name made lowercase.
    fmly_num_4 = models.IntegerField(
        db_column='FMLY_NUM_4', blank=True, null=True)
    # Field name made lowercase.
    fmly_num_5 = models.IntegerField(
        db_column='FMLY_NUM_5', blank=True, null=True)
    # Field name made lowercase.
    fmly_num_6 = models.IntegerField(
        db_column='FMLY_NUM_6', blank=True, null=True)
    # Field name made lowercase.
    fmly_num_7 = models.IntegerField(
        db_column='FMLY_NUM_7', blank=True, null=True)
    # Field name made lowercase.
    fmly_num_8 = models.IntegerField(
        db_column='FMLY_NUM_8', blank=True, null=True)
    # Field name made lowercase.
    fmly_num_9 = models.IntegerField(
        db_column='FMLY_NUM_9', blank=True, null=True)
    # Field name made lowercase.
    fmly_num_10 = models.IntegerField(
        db_column='FMLY_NUM_10', blank=True, null=True)
    # Field name made lowercase.
    fmly_num_11 = models.IntegerField(
        db_column='FMLY_NUM_11', blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    applc_dtime = models.DateTimeField(db_column='APPLC_DTIME')

    class Meta:
        managed = False
        db_table = 'COM_SMPLTAX'
        unique_together = (('std_year', 'salary_above', 'salary_belo'),)


class ComTml(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    model_id = models.CharField(db_column='MODEL_ID', max_length=30)
    # Field name made lowercase.
    tml_instl_num = models.IntegerField(
        db_column='TML_INSTL_NUM', blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_TML'
        unique_together = (('corp_no', 'model_id'),)


class ComTmlhis(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    model_id = models.CharField(db_column='MODEL_ID', max_length=30)
    # Field name made lowercase.
    rev_no = models.IntegerField(db_column='REV_NO')
    # Field name made lowercase.
    tml_instl_num = models.IntegerField(
        db_column='TML_INSTL_NUM', blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_TMLHIS'
        unique_together = (('corp_no', 'model_id', 'rev_no'),)


class ComTmlivntry(models.Model):
    # Field name made lowercase.
    model_id = models.CharField(
        db_column='MODEL_ID', primary_key=True, max_length=30)
    # Field name made lowercase.
    tml_kind = models.CharField(
        db_column='TML_KIND', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    model_nm = models.CharField(
        db_column='MODEL_NM', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    maker = models.CharField(
        db_column='MAKER', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    ivntry_qty = models.IntegerField(
        db_column='IVNTRY_QTY', blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_TMLIVNTRY'


class ComTmlreq(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    model_id = models.CharField(db_column='MODEL_ID', max_length=30)
    # Field name made lowercase.
    req_dtime = models.DateTimeField(db_column='REQ_DTIME')
    # Field name made lowercase.
    req_num = models.IntegerField(db_column='REQ_NUM', blank=True, null=True)
    # Field name made lowercase.
    req_id = models.CharField(
        db_column='REQ_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_TMLREQ'
        unique_together = (('corp_no', 'model_id', 'req_dtime'),)


class ComTmlstock(models.Model):
    # Field name made lowercase.
    model_id = models.CharField(
        db_column='MODEL_ID', primary_key=True, max_length=30)
    # Field name made lowercase.
    stock_dtime = models.DateTimeField(db_column='STOCK_DTIME')
    # Field name made lowercase.
    stock_qty = models.IntegerField(
        db_column='STOCK_QTY', blank=True, null=True)
    # Field name made lowercase.
    chckr_id = models.CharField(
        db_column='CHCKR_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_TMLSTOCK'
        unique_together = (('model_id', 'stock_dtime'),)


class ComTmlunstock(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    model_id = models.CharField(db_column='MODEL_ID', max_length=30)
    # Field name made lowercase.
    unstock_dtime = models.DateTimeField(db_column='UNSTOCK_DTIME')
    # Field name made lowercase.
    unstock_qty = models.IntegerField(
        db_column='UNSTOCK_QTY', blank=True, null=True)
    # Field name made lowercase.
    chckr_id = models.CharField(
        db_column='CHCKR_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COM_TMLUNSTOCK'
        unique_together = (('corp_no', 'model_id', 'unstock_dtime'),)


class EtcTml(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    tml_id = models.IntegerField(db_column='TML_ID')
    # Field name made lowercase.
    tml_nm = models.CharField(
        db_column='TML_NM', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    model_nm = models.CharField(
        db_column='MODEL_NM', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    sn = models.CharField(db_column='SN', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    maker = models.CharField(
        db_column='MAKER', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    instl_loc = models.CharField(
        db_column='INSTL_LOC', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    instl_dtime = models.DateTimeField(
        db_column='INSTL_DTIME', blank=True, null=True)
    # Field name made lowercase.
    state = models.CharField(
        db_column='STATE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ETC_TML'
        unique_together = (('corp_no', 'tml_id'),)


class EtcTmllog(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    empl_no = models.CharField(db_column='EMPL_NO', max_length=50)
    # Field name made lowercase.
    tml_id = models.IntegerField(db_column='TML_ID')
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    rcv_dtime = models.DateTimeField(
        db_column='RCV DTIME', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ETC_TMLLOG'
        unique_together = (('corp_no', 'dept_no', 'empl_no', 'tml_id'),)


class HrmAtend(models.Model):
    # Field name made lowercase.
    empl_no = models.CharField(
        db_column='EMPL_NO', primary_key=True, max_length=50)
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO')
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    base_atendtime = models.TimeField(
        db_column='BASE_ATENDTIME', blank=True, null=True)
    # Field name made lowercase.
    base_lvofctime = models.TimeField(
        db_column='BASE_LVOFCTIME', blank=True, null=True)
    # Field name made lowercase.
    mdwk_workday = models.CharField(
        db_column='MDWK_WORKDAY', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    whday = models.CharField(
        db_column='WHDAY', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    crtlwh = models.IntegerField(db_column='CRTLWH', blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HRM_ATEND'
        unique_together = (('empl_no', 'corp_no', 'dept_no'),)


class HrmAtendhis(models.Model):
    # Field name made lowercase.
    empl_no = models.CharField(
        db_column='EMPL_NO', primary_key=True, max_length=50)
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO')
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    rev_no = models.IntegerField(db_column='REV_NO')
    # Field name made lowercase.
    base_atendtime = models.TimeField(
        db_column='BASE_ATENDTIME', blank=True, null=True)
    # Field name made lowercase.
    base_lvofctime = models.TimeField(
        db_column='BASE_LVOFCTIME', blank=True, null=True)
    # Field name made lowercase.
    mdwk_workday = models.CharField(
        db_column='MDWK_WORKDAY', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    whday = models.CharField(
        db_column='WHDAY', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    crtlwh = models.IntegerField(db_column='CRTLWH', blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HRM_ATENDHIS'
        unique_together = (('empl_no', 'corp_no', 'dept_no', 'rev_no'),)


class HrmEmpl(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    empl_no = models.CharField(db_column='EMPL_NO', max_length=50)
    # Field name made lowercase.
    ofcps = models.CharField(
        db_column='OFCPS', max_length=6, blank=True, null=True)
    # Field name made lowercase.
    empl_nm = models.CharField(
        db_column='EMPL_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    gender = models.CharField(
        db_column='GENDER', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    mrig_yn = models.CharField(
        db_column='MRIG_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    prsl_email = models.CharField(
        db_column='PRSL_EMAIL', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    brthdy = models.DateField(db_column='BRTHDY', blank=True, null=True)
    # Field name made lowercase.
    hffc_state = models.CharField(
        db_column='HFFC_STATE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    exctv_yn = models.CharField(
        db_column='EXCTV_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    photo_id = models.IntegerField(db_column='PHOTO_ID', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    frgnr_yn = models.CharField(
        db_column='FRGNR_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    tel_no = models.CharField(
        db_column='TEL_NO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    mobile_no = models.CharField(
        db_column='MOBILE_NO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    lunisolar = models.CharField(
        db_column='LUNISOLAR', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    retire_date = models.DateField(
        db_column='RETIRE_DATE', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    salary_form = models.CharField(
        db_column='SALARY_FORM', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    ssid = models.CharField(
        db_column='SSID', max_length=13, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='EMAIL', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    emplym_form = models.CharField(
        db_column='EMPLYM_FORM', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    mrig_anvsry = models.DateField(
        db_column='MRIG_ANVSRY', blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    ssid_addr = models.CharField(
        db_column='SSID_ADDR', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    rlrsdnc_addr = models.CharField(
        db_column='RLRSDNC_ADDR', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    encpnd = models.DateField(db_column='ENCPND', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HRM_EMPL'
        unique_together = (('corp_no', 'dept_no', 'empl_no'),)


class HrmEmplhis(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    empl_no = models.CharField(db_column='EMPL_NO', max_length=50)
    # Field name made lowercase.
    rev_no = models.IntegerField(db_column='REV_NO')
    # Field name made lowercase.
    empl_nm = models.CharField(
        db_column='EMPL_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    ssid = models.CharField(
        db_column='SSID', max_length=13, blank=True, null=True)
    # Field name made lowercase.
    gender = models.CharField(
        db_column='GENDER', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    brthdy = models.DateField(db_column='BRTHDY', blank=True, null=True)
    # Field name made lowercase.
    lunisolar = models.CharField(
        db_column='LUNISOLAR', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    mrig_yn = models.CharField(
        db_column='MRIG_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    mrig_anvsry = models.DateField(
        db_column='MRIG_ANVSRY', blank=True, null=True)
    # Field name made lowercase.
    tel_no = models.CharField(
        db_column='TEL_NO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    mobile_no = models.CharField(
        db_column='MOBILE_NO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    ssid_addr = models.CharField(
        db_column='SSID_ADDR', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    rlrsdnc_addr = models.CharField(
        db_column='RLRSDNC_ADDR', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='EMAIL', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    prsl_email = models.CharField(
        db_column='PRSL_EMAIL', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    exctv_yn = models.CharField(
        db_column='EXCTV_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    ofcps = models.CharField(
        db_column='OFCPS', max_length=6, blank=True, null=True)
    # Field name made lowercase.
    emplym_form = models.CharField(
        db_column='EMPLYM_FORM', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    salary_form = models.CharField(
        db_column='SALARY_FORM', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    encpnd = models.DateField(db_column='ENCPND', blank=True, null=True)
    # Field name made lowercase.
    hffc_state = models.CharField(
        db_column='HFFC_STATE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    retire_date = models.DateField(
        db_column='RETIRE_DATE', blank=True, null=True)
    # Field name made lowercase.
    frgnr_yn = models.CharField(
        db_column='FRGNR_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HRM_EMPLHIS'
        unique_together = (('corp_no', 'dept_no', 'empl_no', 'rev_no'),)


class HrmFmly(models.Model):
    # Field name made lowercase.
    empl_no = models.CharField(
        db_column='EMPL_NO', primary_key=True, max_length=50)
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO')
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    fmly_no = models.IntegerField(db_column='FMLY_NO')
    # Field name made lowercase.
    constnt_type = models.CharField(
        db_column='CONSTNT_TYPE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    reltn = models.CharField(
        db_column='RELTN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    constnt_nm = models.CharField(
        db_column='CONSTNT_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    brthdy = models.DateField(db_column='BRTHDY', blank=True, null=True)
    # Field name made lowercase.
    livtgt_yn = models.CharField(
        db_column='LIVTGT_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    dednhope_yn = models.CharField(
        db_column='DEDNHOPE_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    dspsn_yn = models.CharField(
        db_column='DSPSN_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    state = models.CharField(
        db_column='STATE', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HRM_FMLY'
        unique_together = (('empl_no', 'corp_no', 'dept_no', 'fmly_no'),)


class HrmFrgnr(models.Model):
    # Field name made lowercase.
    empl_no = models.CharField(
        db_column='EMPL_NO', primary_key=True, max_length=50)
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO')
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    dtrmcexp_date = models.DateField(
        db_column='DTRMCEXP_DATE', blank=True, null=True)
    # Field name made lowercase.
    dtrmcexp_icny = models.CharField(
        db_column='DTRMCEXP_ICNY', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    dtrmcexp_insrnc_amt = models.DecimalField(
        db_column='DTRMCEXP_INSRNC_AMT', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HRM_FRGNR'
        unique_together = (('empl_no', 'corp_no', 'dept_no'),)


class HrmFrgnrhis(models.Model):
    # Field name made lowercase.
    empl_no = models.CharField(
        db_column='EMPL_NO', primary_key=True, max_length=50)
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO')
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    rev_no = models.IntegerField(db_column='REV_NO')
    # Field name made lowercase.
    dtrmcexp_date = models.DateField(
        db_column='DTRMCEXP_DATE', blank=True, null=True)
    # Field name made lowercase.
    dtrmcexp_icny = models.CharField(
        db_column='DTRMCEXP_ICNY', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    dtrmcexp_insrnc_amt = models.DecimalField(
        db_column='DTRMCEXP_INSRNC_AMT', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HRM_FRGNRHIS'
        unique_together = (('empl_no', 'corp_no', 'dept_no', 'rev_no'),)


class HrmSalary(models.Model):
    # Field name made lowercase.
    empl_no = models.CharField(
        db_column='EMPL_NO', primary_key=True, max_length=50)
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO')
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    base_salary = models.DecimalField(
        db_column='BASE_SALARY', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    trn_bank = models.CharField(
        db_column='TRN_BANK', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    acc_no = models.CharField(
        db_column='ACC_NO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    npn_pay_yn = models.CharField(
        db_column='NPN_PAY_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    npn_mrmrtn = models.DecimalField(
        db_column='NPN_MRMRTN', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    hlthins_pay_yn = models.CharField(
        db_column='HLTHINS_PAY_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    hlthins_mrmrtn = models.DecimalField(
        db_column='HLTHINS_MRMRTN', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    empins_pay_yn = models.CharField(
        db_column='EMPINS_PAY_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    rperins_pay_yn = models.CharField(
        db_column='RPERINS_PAY_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    wthtx_taxrt = models.DecimalField(
        db_column='WTHTX_TAXRT', max_digits=5, decimal_places=3, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HRM_SALARY'
        unique_together = (('empl_no', 'corp_no', 'dept_no'),)


class HrmSalaryhis(models.Model):
    # Field name made lowercase.
    empl_no = models.CharField(
        db_column='EMPL_NO', primary_key=True, max_length=50)
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO')
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    rev_no = models.IntegerField(db_column='REV_NO')
    # Field name made lowercase.
    base_salary = models.DecimalField(
        db_column='BASE_SALARY', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    trn_bank = models.CharField(
        db_column='TRN_BANK', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    acc_no = models.CharField(
        db_column='ACC_NO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    npn_pay_yn = models.CharField(
        db_column='NPN_PAY_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    npn_mrmrtn = models.DecimalField(
        db_column='NPN_MRMRTN', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    hlthins_pay_yn = models.CharField(
        db_column='HLTHINS_PAY_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    hlthins_mrmrtn = models.DecimalField(
        db_column='HLTHINS_MRMRTN', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    empins_pay_yn = models.CharField(
        db_column='EMPINS_PAY_YN', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    empins_mrmrtn = models.DecimalField(
        db_column='EMPINS_MRMRTN', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HRM_SALARYHIS'
        unique_together = (('empl_no', 'corp_no', 'dept_no', 'rev_no'),)


class HtmEmplphoto(models.Model):
    # Field name made lowercase.
    photo_id = models.IntegerField(db_column='PHOTO_ID', primary_key=True)
    # Field name made lowercase.
    file_org_nm = models.CharField(
        db_column='FILE_ORG_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    file_modify_nm = models.CharField(
        db_column='FILE_MODIFY_NM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    file_path = models.CharField(
        db_column='FILE_PATH', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    file_size = models.IntegerField(
        db_column='FILE_SIZE', blank=True, null=True)
    # Field name made lowercase.
    crt_dtime = models.DateTimeField(
        db_column='CRT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HTM_EMPLPHOTO'


class SlmAnntydtl(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    empl_no = models.CharField(db_column='EMPL_NO', max_length=50)
    # Field name made lowercase.
    salary_ymon = models.CharField(db_column='SALARY_YMON', max_length=6)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    frgnr_yn = models.CharField(
        db_column='FRGNR YN', max_length=1, blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    anntypay_num = models.IntegerField(
        db_column='ANNTYPAY NUM', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    anntypay_amt = models.DecimalField(
        db_column='ANNTYPAY AMT', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    dtrmcexp_icny = models.CharField(
        db_column='DTRMCEXP ICNY', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SLM_ANNTYDTL'
        unique_together = (('corp_no', 'dept_no', 'empl_no', 'salary_ymon'),)


class SlmSalary(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    empl_no = models.CharField(db_column='EMPL_NO', max_length=50)
    # Field name made lowercase.
    salary_ymon = models.CharField(db_column='SALARY_YMON', max_length=6)
    # Field name made lowercase.
    salary_kind = models.CharField(
        db_column='SALARY_KIND', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    salarypay_sum = models.DecimalField(
        db_column='SALARYPAY_SUM', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    speclalnc_sum = models.DecimalField(
        db_column='SPECLALNC_SUM', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    dedn_sum = models.DecimalField(
        db_column='DEDN_SUM', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    salary_payamt = models.DecimalField(
        db_column='SALARY_PAYAMT', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    trn_date = models.DateField(db_column='TRN_DATE', blank=True, null=True)
    # Field name made lowercase.
    remark = models.CharField(
        db_column='REMARK', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SLM_SALARY'
        unique_together = (('corp_no', 'dept_no', 'empl_no', 'salary_ymon'),)


class SlmSalarydtl(models.Model):
    # Field name made lowercase.
    corp_no = models.IntegerField(db_column='CORP_NO', primary_key=True)
    # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6)
    # Field name made lowercase.
    empl_no = models.CharField(db_column='EMPL_NO', max_length=50)
    # Field name made lowercase.
    salary_ymon = models.CharField(db_column='SALARY_YMON', max_length=6)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_type = models.CharField(
        db_column='ITEM TYPE', max_length=4, blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_cd = models.CharField(
        db_column='ITEM CD', max_length=4, blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_nm = models.CharField(
        db_column='ITEM NM', max_length=30, blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    sort_seq = models.IntegerField(db_column='SORT SEQ', blank=True, null=True)
    # Field name made lowercase.
    amt = models.DecimalField(
        db_column='AMT', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    reg_dtime = models.DateTimeField(
        db_column='REG_DTIME', blank=True, null=True)
    # Field name made lowercase.
    reg_id = models.CharField(
        db_column='REG_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    upt_dtime = models.DateTimeField(
        db_column='UPT_DTIME', blank=True, null=True)
    # Field name made lowercase.
    upt_id = models.CharField(
        db_column='UPT_ID', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SLM_SALARYDTL'
        unique_together = (('corp_no', 'dept_no', 'empl_no', 'salary_ymon'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
