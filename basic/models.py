# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Airport(models.Model):
    air_name = models.CharField(db_column='AIR_NAME', primary_key=True, max_length=20, blank=True, null=False)  # Field name made lowercase.
    air_lat = models.TextField(db_column='AIR_LAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    air_lng = models.TextField(db_column='AIR_LNG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    city_name = models.CharField(db_column='CITY_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    coun_pic = models.TextField(db_column='COUN_PIC', blank=True, null=True)  # Field name made lowercase.
    city_info1 = models.TextField(db_column='CITY_INFO1', blank=True, null=True)  # Field name made lowercase.
    city_info2 = models.TextField(db_column='CITY_INFO2', blank=True, null=True)  # Field name made lowercase.
    city_info3 = models.TextField(db_column='CITY_INFO3', blank=True, null=True)  # Field name made lowercase.
    city_eng = models.CharField(db_column='CITY_ENG', max_length=20, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'AIRPORT'


class Attraction(models.Model):
    attract_id = models.TextField(db_column='ATTRACT_ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    city_name = models.CharField(db_column='CITY_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    a_name = models.CharField(db_column='A_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    a_info = models.TextField(db_column='A_INFO', blank=True, null=True)  # Field name made lowercase.
    country_name = models.TextField(db_column='COUNTRY_NAME', blank=True, null=True)  # Field name made lowercase.
    a_pic = models.TextField(db_column='A_PIC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATTRACTION'


class Country(models.Model):
    country_name = models.TextField(db_column='COUNTRY_NAME', primary_key=True, blank=True, null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COUNTRY'


class Customer(models.Model):
    cus_id = models.TextField(db_column='CUS_ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    cus_pass = models.CharField(db_column='CUS_PASS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cus_email = models.CharField(db_column='CUS_EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cus_name = models.CharField(db_column='CUS_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sns_login = models.CharField(db_column='SNS_LOGIN', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMER'


class Eurail(models.Model):
    eurail_id = models.TextField(db_column='EURAIL_ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    r_origin = models.CharField(db_column='R_ORIGIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    r_dest = models.CharField(db_column='R_DEST', max_length=20, blank=True, null=True)  # Field name made lowercase.
    r_origin_city = models.CharField(db_column='R_ORIGIN_CITY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    r_dest_city = models.CharField(db_column='R_DEST_CITY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dep_date = models.TextField(db_column='DEP_DATE', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    dep_time = models.CharField(db_column='DEP_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    arr_time = models.CharField(db_column='ARR_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    required_time = models.CharField(db_column='REQUIRED_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EURAIL'


class Event(models.Model):
    event_id = models.CharField(db_column='EVENT_ID', primary_key=True, max_length=20, blank=True, null=False)  # Field name made lowercase.
    event_type = models.CharField(db_column='EVENT_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    e_name = models.CharField(db_column='E_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    e_place = models.CharField(db_column='E_PLACE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    e_date = models.CharField(db_column='E_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    e_info = models.TextField(db_column='E_INFO', blank=True, null=True)  # Field name made lowercase.
    country_name = models.CharField(db_column='COUNTRY_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    e_pic = models.TextField(db_column='E_PIC', blank=True, null=True)  # Field name made lowercase.
    e_s_date = models.DateField(db_column='E_S_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT'


class Food(models.Model):
    food_id = models.TextField(db_column='FOOD_ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    f_name = models.TextField(db_column='F_NAME', blank=True, null=True)  # Field name made lowercase.
    f_info = models.TextField(db_column='F_INFO', blank=True, null=True)  # Field name made lowercase.
    country_name = models.TextField(db_column='COUNTRY_NAME', blank=True, null=True)  # Field name made lowercase.
    f_pic = models.TextField(db_column='F_PIC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FOOD'


class Listdetail(models.Model):
    route_id = models.TextField(db_column='ROUTE_ID', blank=False, null=False)  # Field name made lowercase.
    cost = models.IntegerField(db_column='COST', blank=True, null=True)  # Field name made lowercase.
    airline = models.CharField(db_column='AIRLINE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dep_date = models.TextField(db_column='DEP_DATE', blank=True, null=True)  # Field name made lowercase.
    arr_date = models.TextField(db_column='ARR_DATE', blank=True, null=True)  # Field name made lowercase.
    dep_time = models.DateField(db_column='DEP_TIME', blank=True, null=True)  # Field name made lowercase.
    arr_time = models.CharField(db_column='ARR_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    r_origin = models.CharField(db_column='R_ORIGIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    r_dest = models.CharField(db_column='R_DEST', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stop_num = models.CharField(db_column='STOP_NUM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flight_time = models.TextField(db_column='FLIGHT_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    list_id = models.IntegerField(db_column='LIST_ID', blank=False, null=False)  # Field name made lowercase.
    second_dep = models.TextField(db_column='SECOND_DEP', blank=False, null=False)  # Field name made lowercase.
    second_arr = models.TextField(db_column='SECOND_ARR', blank=False, null=False)  # Field name made lowercase.
    second_duration = models.CharField(db_column='SECOND_DURATION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    layover = models.CharField(db_column='LAYOVER', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTDETAIL'
        unique_together = (('route_id', 'list_id'),)


class Mylist(models.Model):
    list_id = models.IntegerField(db_column='LIST_ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    total_cost = models.IntegerField(db_column='TOTAL_COST', blank=True, null=True)  # Field name made lowercase.
    dep_date = models.DateField(db_column='DEP_DATE', blank=True, null=True)  # Field name made lowercase.
    arr_date = models.DateField(db_column='ARR_DATE', blank=True, null=True)  # Field name made lowercase.
    dep_time = models.CharField(db_column='DEP_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    arr_time = models.CharField(db_column='ARR_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    save_date = models.DateField(db_column='SAVE_DATE', blank=True, null=True, auto_now = True)  # Field name made lowercase.
    city_1 = models.CharField(db_column='CITY_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city_2 = models.CharField(db_column='CITY_2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city_3 = models.CharField(db_column='CITY_3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city_4 = models.CharField(db_column='CITY_4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city_5 = models.CharField(db_column='CITY_5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city_6 = models.CharField(db_column='CITY_6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city_7 = models.CharField(db_column='CITY_7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city_8 = models.CharField(db_column='CITY_8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stay_1 = models.CharField(db_column='STAY_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stay_2 = models.CharField(db_column='STAY_2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stay_3 = models.CharField(db_column='STAY_3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stay_4 = models.CharField(db_column='STAY_4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stay_5 = models.CharField(db_column='STAY_5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stay_6 = models.CharField(db_column='STAY_6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stay_7 = models.CharField(db_column='STAY_7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stay_8 = models.CharField(db_column='STAY_8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MYLIST'

class Route(models.Model):
    route_id = models.TextField(db_column='ROUTE_ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    r_origin = models.TextField(db_column='R_ORIGIN', blank=True, null=True)  # Field name made lowercase.
    r_dest = models.TextField(db_column='R_DEST', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROUTE'


class Trend(models.Model):
    trend_id = models.TextField(db_column='TREND_ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    daysleft = models.IntegerField(db_column='DAYSLEFT', blank=True, null=True)  # Field name made lowercase.
    cost = models.TextField(db_column='COST', blank=True, null=True)  # Field name made lowercase.
    route_id = models.TextField(db_column='ROUTE_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TREND'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Csv(models.Model):
    r_dest = models.TextField(db_column='R_DEST', blank=True, null=True)  # Field name made lowercase.
    arr_t = models.TextField(db_column='ARR_T', blank=True, null=True)  # Field name made lowercase.
    stop_num = models.TextField(db_column='STOP_NUM', blank=True, null=True)  # Field name made lowercase.
    dep_t = models.TextField(db_column='DEP_T', blank=True, null=True)  # Field name made lowercase.
    r_origin = models.TextField(db_column='R_ORIGIN', blank=True, null=True)  # Field name made lowercase.
    sch_cost = models.IntegerField(db_column='SCH_COST', blank=True, null=True)  # Field name made lowercase.
    l_lo = models.TextField(db_column='L_LO', blank=True, null=True)  # Field name made lowercase.
    f_time = models.TextField(db_column='F_TIME', blank=True, null=True)  # Field name made lowercase.
    arr_day = models.TextField(db_column='ARR_DAY', blank=True, null=True)  # Field name made lowercase.
    arr_d_week = models.TextField(db_column='ARR_D_WEEK', blank=True, null=True)  # Field name made lowercase.
    dep_day = models.TextField(db_column='DEP_DAY', blank=True, null=True)  # Field name made lowercase.
    dep_d_week = models.TextField(db_column='DEP_D_WEEK', blank=True, null=True)  # Field name made lowercase.
    no = models.IntegerField(primary_key=True, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'csv'


class DemoPerson(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'demo_person'


class DemoScrapy1(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sch_cost = models.PositiveSmallIntegerField(db_column='SCH_COST')  # Field name made lowercase.
    air_info = models.TextField(db_column='AIR_INFO')  # Field name made lowercase.
    r_origin = models.TextField(db_column='R_ORIGIN')  # Field name made lowercase.
    dep_date = models.DateField(db_column='DEP_DATE')  # Field name made lowercase.
    r_dest = models.TextField(db_column='R_DEST')  # Field name made lowercase.
    arr_t = models.TextField(db_column='ARR_T')  # Field name made lowercase.
    l_lo = models.TextField(db_column='L_LO')  # Field name made lowercase.
    dep_t = models.TextField(db_column='DEP_T')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'demo_scrapy1'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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
