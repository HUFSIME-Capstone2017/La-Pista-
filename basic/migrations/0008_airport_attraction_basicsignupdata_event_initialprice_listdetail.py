# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-21 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0007_auto_20170509_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('air_name', models.CharField(blank=True, db_column='AIR_NAME', max_length=20, primary_key=True, serialize=False)),
                ('air_lat', models.TextField(blank=True, db_column='AIR_LAT', null=True)),
                ('air_lng', models.TextField(blank=True, db_column='AIR_LNG', null=True)),
                ('city_name', models.CharField(blank=True, db_column='CITY_NAME', max_length=20, null=True)),
                ('coun_pic', models.TextField(blank=True, db_column='COUN_PIC', null=True)),
            ],
            options={
                'db_table': 'AIRPORT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('attract_id', models.TextField(blank=True, db_column='ATTRACT_ID', primary_key=True, serialize=False)),
                ('city_name', models.CharField(blank=True, db_column='CITY_NAME', max_length=20, null=True)),
                ('a_name', models.CharField(blank=True, db_column='A_NAME', max_length=20, null=True)),
                ('a_info', models.TextField(blank=True, db_column='A_INFO', null=True)),
                ('country_name', models.TextField(blank=True, db_column='COUNTRY_NAME', null=True)),
                ('a_pic', models.TextField(blank=True, db_column='A_PIC', null=True)),
            ],
            options={
                'db_table': 'ATTRACTION',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BasicSignUpData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=40)),
                ('number', models.IntegerField()),
                ('country', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'basic_sign_up_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.CharField(blank=True, db_column='EVENT_ID', max_length=20, primary_key=True, serialize=False)),
                ('event_type', models.CharField(blank=True, db_column='EVENT_TYPE', max_length=20, null=True)),
                ('e_name', models.CharField(blank=True, db_column='E_NAME', max_length=20, null=True)),
                ('e_place', models.CharField(blank=True, db_column='E_PLACE', max_length=20, null=True)),
                ('e_date', models.CharField(blank=True, db_column='E_DATE', max_length=20, null=True)),
                ('e_info', models.TextField(blank=True, db_column='E_INFO', null=True)),
                ('country_name', models.CharField(blank=True, db_column='COUNTRY_NAME', max_length=20, null=True)),
                ('e_pic', models.TextField(blank=True, db_column='E_PIC', null=True)),
                ('e_s_date', models.DateField(blank=True, db_column='E_S_DATE', null=True)),
            ],
            options={
                'db_table': 'EVENT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Initialprice',
            fields=[
                ('initial_id', models.TextField(blank=True, db_column='INITIAL_ID', primary_key=True, serialize=False)),
                ('initial_date', models.DateField(blank=True, db_column='INITIAL_DATE', null=True)),
                ('initial_cost', models.TextField(blank=True, db_column='INITIAL_COST', null=True)),
                ('route_id', models.TextField(blank=True, db_column='ROUTE_ID', null=True)),
            ],
            options={
                'db_table': 'INITIALPRICE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Listdetail',
            fields=[
                ('route_id', models.TextField(blank=True, db_column='ROUTE_ID', primary_key=True, serialize=False)),
                ('cost', models.IntegerField(blank=True, db_column='COST', null=True)),
                ('airline', models.CharField(blank=True, db_column='AIRLINE', max_length=50, null=True)),
                ('dep_date', models.TextField(blank=True, db_column='DEP_DATE', null=True)),
                ('arr_date', models.TextField(blank=True, db_column='ARR_DATE', null=True)),
                ('dep_time', models.DateField(blank=True, db_column='DEP_TIME', null=True)),
                ('arr_time', models.CharField(blank=True, db_column='ARR_TIME', max_length=20, null=True)),
                ('r_origin', models.CharField(blank=True, db_column='R_ORIGIN', max_length=20, null=True)),
                ('r_dest', models.CharField(blank=True, db_column='R_DEST', max_length=20, null=True)),
                ('stop_num', models.TextField(blank=True, db_column='STOP_NUM', null=True)),
                ('flight_time', models.TextField(blank=True, db_column='FLIGHT_TIME', null=True)),
                ('list_id', models.IntegerField(blank=True, db_column='LIST_ID', primary_key=True)),
            ],
            options={
                'db_table': 'LISTDETAIL',
                'managed': False,
            },
        ),
    ]