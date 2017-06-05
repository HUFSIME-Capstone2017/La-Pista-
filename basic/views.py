# -*- coding: utf-8 -*-
#import http.client
import json
from django.shortcuts import render
from django.http	import HttpResponse
from django.views.decorators.csrf import csrf_protect
from basic import models
from django.shortcuts import render_to_response
import cplex
import pandas as pd
import numpy as np
import sqlite3
import json
import requests
from math import fabs
from deftsp import deftsp
from ordertsp import order
from basic.forms import *
from .forms import UserForm
from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,authenticate
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.contrib.auth import logout
from django.http import HttpRequest,HttpResponse
from django.http import JsonResponse
from json import dumps
from django.core import serializers
import datetime
from datetime import *

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/main')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('/index')
    else:
        form = UserForm()
        return render(request, 'pages/signup.html', {'form': form})

def signin(request):
    if request.method == "POST":
        form1 = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form1 = LoginForm()
        return render(request, 'pages/login.html', {'form1': form1})

def index(request):
    return render(request, 'pages/index.html')

def main(request):
	adult_num = [
	{"label": "0", "value": "0"},
	{"label": "1", "value": "1"},
	{"label": "2", "value": "2"},
	{"label": "3", "value": "3"},
	{"label": "4", "value": "4"},
	{"label": "5", "value": "5"},
	{"label": "6", "value": "6"},
	{"label": "7", "value": "7"},
	{"label": "8", "value": "8"},
	{"label": "9", "value": "9"}
	]
	selected_value = "1"

	kid_num = [
	{"label": "0", "value": "0"},
	{"label": "1", "value": "1"},
	{"label": "2", "value": "2"},
	{"label": "3", "value": "3"},
	{"label": "4", "value": "4"},
	{"label": "5", "value": "5"},
	{"label": "6", "value": "6"},
	{"label": "7", "value": "7"},
	{"label": "8", "value": "8"},
	{"label": "9", "value": "9"}
	]
	selected_value_kids = "0"

	return render(request, 'pages/main.html',  {"adult_num": adult_num,
												"selected_value": selected_value,
												"kid_num": kid_num,
												"selected_value_kids": selected_value_kids,
												'food_france' : models.Food.objects.filter(country_name = '프랑스'),
                                    			'event_france': models.Event.objects.filter(country_name = '프랑스'),
                                   				'att_france' : models.Attraction.objects.filter(country_name='프랑스'),
                                   				'food_net' : models.Food.objects.filter(country_name = '네덜란드'),
                                    			'event_net': models.Event.objects.filter(country_name = '네덜란드'),
                                   				'att_net' : models.Attraction.objects.filter(country_name='네덜란드'),
                                   				'food_spain' : models.Food.objects.filter(country_name = '스페인'),
                                    			'event_spain': models.Event.objects.filter(country_name = '스페인'),
                                   				'att_spain' : models.Attraction.objects.filter(country_name='스페인'),
                                   				'food_bul' : models.Food.objects.filter(country_name = '불가리아'),
                                    			'event_bul': models.Event.objects.filter(country_name = '불가리아'),
                                   				'att_bul' : models.Attraction.objects.filter(country_name='불가리아'),
                                   				'food_ger' : models.Food.objects.filter(country_name = '독일'),
                                    			'event_ger': models.Event.objects.filter(country_name = '독일'),
                                   				'att_ger' : models.Attraction.objects.filter(country_name='독일'),
                                   				'food_ruma' : models.Food.objects.filter(country_name = '루마니아'),
                                    			'event_ruma': models.Event.objects.filter(country_name = '루마니아'),
                                   				'att_ruma' : models.Attraction.objects.filter(country_name='루마니아'),
                                   				'food_bel' : models.Food.objects.filter(country_name = '벨기에'),
                                    			'event_bel': models.Event.objects.filter(country_name = '벨기에'),
                                   				'att_bel' : models.Attraction.objects.filter(country_name='벨기에'),
                                   				'food_swi' : models.Food.objects.filter(country_name = '스위스'),
                                    			'event_swi': models.Event.objects.filter(country_name = '스위스'),
                                   				'att_swi' : models.Attraction.objects.filter(country_name='스위스'),
                                   				'food_isl' : models.Food.objects.filter(country_name = '아일랜드'),
                                    			'event_isl': models.Event.objects.filter(country_name = '아일랜드'),
                                   				'att_isl' : models.Attraction.objects.filter(country_name='아일랜드'),
                                   				'food_bri' : models.Food.objects.filter(country_name = '영국'),
                                    			'event_bri': models.Event.objects.filter(country_name = '영국'),
                                   				'att_bri' : models.Attraction.objects.filter(country_name='영국'),
                                   				'food_cze' : models.Food.objects.filter(country_name = '체코'),
                                    			'event_cze': models.Event.objects.filter(country_name = '체코'),
                                   				'att_cze' : models.Attraction.objects.filter(country_name='체코'),
                                   				'food_ita' : models.Food.objects.filter(country_name = '이탈리아'),
                                    			'event_ita': models.Event.objects.filter(country_name = '이탈리아'),
                                   				'att_ita' : models.Attraction.objects.filter(country_name='이탈리아'),
                                   				'food_por' : models.Food.objects.filter(country_name = '포르투갈'),
                                    			'event_por': models.Event.objects.filter(country_name = '포르투갈'),
                                   				'att_por' : models.Attraction.objects.filter(country_name='포르투갈'),
                                   				'food_pol' : models.Food.objects.filter(country_name = '폴란드'),
                                    			'event_pol': models.Event.objects.filter(country_name = '폴란드'),
                                   				'att_pol' : models.Attraction.objects.filter(country_name='폴란드'),
                                   				'food_hun' : models.Food.objects.filter(country_name = '헝가리'),
                                    			'event_hun': models.Event.objects.filter(country_name = '헝가리'),
                                   				'att_hun' : models.Attraction.objects.filter(country_name='헝가리'),
												})

def emain(request):
	adult_num = [
	{"label": "0", "value": "0"},
	{"label": "1", "value": "1"},
	{"label": "2", "value": "2"},
	{"label": "3", "value": "3"},
	{"label": "4", "value": "4"},
	{"label": "5", "value": "5"},
	{"label": "6", "value": "6"},
	{"label": "7", "value": "7"},
	{"label": "8", "value": "8"},
	{"label": "9", "value": "9"}
	]
	selected_value = "1"

	kid_num = [
	{"label": "0", "value": "0"},
	{"label": "1", "value": "1"},
	{"label": "2", "value": "2"},
	{"label": "3", "value": "3"},
	{"label": "4", "value": "4"},
	{"label": "5", "value": "5"},
	{"label": "6", "value": "6"},
	{"label": "7", "value": "7"},
	{"label": "8", "value": "8"},
	{"label": "9", "value": "9"}
	]
	selected_value_kids = "0"
	return render(request, 'pages/2main.html',		{"adult_num": adult_num,
													"selected_value": selected_value,
													"kid_num": kid_num,
													"selected_value_kids": selected_value_kids,
													'food_france' : models.Food.objects.filter(country_name = '프랑스'),
	                                    			'event_france': models.Event.objects.filter(country_name = '프랑스'),
	                                   				'att_france' : models.Attraction.objects.filter(country_name='프랑스'),
	                                   				'food_net' : models.Food.objects.filter(country_name = '네덜란드'),
	                                    			'event_net': models.Event.objects.filter(country_name = '네덜란드'),
	                                   				'att_net' : models.Attraction.objects.filter(country_name='네덜란드'),
	                                   				'food_spain' : models.Food.objects.filter(country_name = '스페인'),
	                                    			'event_spain': models.Event.objects.filter(country_name = '스페인'),
	                                   				'att_spain' : models.Attraction.objects.filter(country_name='스페인'),
	                                   				'food_bul' : models.Food.objects.filter(country_name = '불가리아'),
	                                    			'event_bul': models.Event.objects.filter(country_name = '불가리아'),
	                                   				'att_bul' : models.Attraction.objects.filter(country_name='불가리아'),
	                                   				'food_ger' : models.Food.objects.filter(country_name = '독일'),
	                                    			'event_ger': models.Event.objects.filter(country_name = '독일'),
	                                   				'att_ger' : models.Attraction.objects.filter(country_name='독일'),
	                                   				'food_ruma' : models.Food.objects.filter(country_name = '루마니아'),
	                                    			'event_ruma': models.Event.objects.filter(country_name = '루마니아'),
	                                   				'att_ruma' : models.Attraction.objects.filter(country_name='루마니아'),
	                                   				'food_bel' : models.Food.objects.filter(country_name = '벨기에'),
	                                    			'event_bel': models.Event.objects.filter(country_name = '벨기에'),
	                                   				'att_bel' : models.Attraction.objects.filter(country_name='벨기에'),
	                                   				'food_swi' : models.Food.objects.filter(country_name = '스위스'),
	                                    			'event_swi': models.Event.objects.filter(country_name = '스위스'),
	                                   				'att_swi' : models.Attraction.objects.filter(country_name='스위스'),
	                                   				'food_isl' : models.Food.objects.filter(country_name = '아일랜드'),
	                                    			'event_isl': models.Event.objects.filter(country_name = '아일랜드'),
	                                   				'att_isl' : models.Attraction.objects.filter(country_name='아일랜드'),
	                                   				'food_bri' : models.Food.objects.filter(country_name = '영국'),
	                                    			'event_bri': models.Event.objects.filter(country_name = '영국'),
	                                   				'att_bri' : models.Attraction.objects.filter(country_name='영국'),
	                                   				'food_cze' : models.Food.objects.filter(country_name = '체코'),
	                                    			'event_cze': models.Event.objects.filter(country_name = '체코'),
	                                   				'att_cze' : models.Attraction.objects.filter(country_name='체코'),
	                                   				'food_ita' : models.Food.objects.filter(country_name = '이탈리아'),
	                                    			'event_ita': models.Event.objects.filter(country_name = '이탈리아'),
	                                   				'att_ita' : models.Attraction.objects.filter(country_name='이탈리아'),
	                                   				'food_por' : models.Food.objects.filter(country_name = '포르투갈'),
	                                    			'event_por': models.Event.objects.filter(country_name = '포르투갈'),
	                                   				'att_por' : models.Attraction.objects.filter(country_name='포르투갈'),
	                                   				'food_pol' : models.Food.objects.filter(country_name = '폴란드'),
	                                    			'event_pol': models.Event.objects.filter(country_name = '폴란드'),
	                                   				'att_pol' : models.Attraction.objects.filter(country_name='폴란드'),
	                                   				'food_hun' : models.Food.objects.filter(country_name = '헝가리'),
	                                    			'event_hun': models.Event.objects.filter(country_name = '헝가리'),
	                                   				'att_hun' : models.Attraction.objects.filter(country_name='헝가리'),
													})

def westernmain(request):
	adult_num = [
	{"label": "0", "value": "0"},
	{"label": "1", "value": "1"},
	{"label": "2", "value": "2"},
	{"label": "3", "value": "3"},
	{"label": "4", "value": "4"},
	{"label": "5", "value": "5"},
	{"label": "6", "value": "6"},
	{"label": "7", "value": "7"},
	{"label": "8", "value": "8"},
	{"label": "9", "value": "9"}
	]
	selected_value = "1"

	kid_num = [
	{"label": "0", "value": "0"},
	{"label": "1", "value": "1"},
	{"label": "2", "value": "2"},
	{"label": "3", "value": "3"},
	{"label": "4", "value": "4"},
	{"label": "5", "value": "5"},
	{"label": "6", "value": "6"},
	{"label": "7", "value": "7"},
	{"label": "8", "value": "8"},
	{"label": "9", "value": "9"}
	]
	selected_value_kids = "0"
	return render(request, 'pages/westernmain.html',{"adult_num": adult_num,
													"selected_value": selected_value,
													"kid_num": kid_num,
													"selected_value_kids": selected_value_kids,
													'food_france' : models.Food.objects.filter(country_name = '프랑스'),
	                                    			'event_france': models.Event.objects.filter(country_name = '프랑스'),
	                                   				'att_france' : models.Attraction.objects.filter(country_name='프랑스'),
	                                   				'food_net' : models.Food.objects.filter(country_name = '네덜란드'),
	                                    			'event_net': models.Event.objects.filter(country_name = '네덜란드'),
	                                   				'att_net' : models.Attraction.objects.filter(country_name='네덜란드'),
	                                   				'food_spain' : models.Food.objects.filter(country_name = '스페인'),
	                                    			'event_spain': models.Event.objects.filter(country_name = '스페인'),
	                                   				'att_spain' : models.Attraction.objects.filter(country_name='스페인'),
	                                   				'food_bul' : models.Food.objects.filter(country_name = '불가리아'),
	                                    			'event_bul': models.Event.objects.filter(country_name = '불가리아'),
	                                   				'att_bul' : models.Attraction.objects.filter(country_name='불가리아'),
	                                   				'food_ger' : models.Food.objects.filter(country_name = '독일'),
	                                    			'event_ger': models.Event.objects.filter(country_name = '독일'),
	                                   				'att_ger' : models.Attraction.objects.filter(country_name='독일'),
	                                   				'food_ruma' : models.Food.objects.filter(country_name = '루마니아'),
	                                    			'event_ruma': models.Event.objects.filter(country_name = '루마니아'),
	                                   				'att_ruma' : models.Attraction.objects.filter(country_name='루마니아'),
	                                   				'food_bel' : models.Food.objects.filter(country_name = '벨기에'),
	                                    			'event_bel': models.Event.objects.filter(country_name = '벨기에'),
	                                   				'att_bel' : models.Attraction.objects.filter(country_name='벨기에'),
	                                   				'food_swi' : models.Food.objects.filter(country_name = '스위스'),
	                                    			'event_swi': models.Event.objects.filter(country_name = '스위스'),
	                                   				'att_swi' : models.Attraction.objects.filter(country_name='스위스'),
	                                   				'food_isl' : models.Food.objects.filter(country_name = '아일랜드'),
	                                    			'event_isl': models.Event.objects.filter(country_name = '아일랜드'),
	                                   				'att_isl' : models.Attraction.objects.filter(country_name='아일랜드'),
	                                   				'food_bri' : models.Food.objects.filter(country_name = '영국'),
	                                    			'event_bri': models.Event.objects.filter(country_name = '영국'),
	                                   				'att_bri' : models.Attraction.objects.filter(country_name='영국'),
	                                   				'food_cze' : models.Food.objects.filter(country_name = '체코'),
	                                    			'event_cze': models.Event.objects.filter(country_name = '체코'),
	                                   				'att_cze' : models.Attraction.objects.filter(country_name='체코'),
	                                   				'food_ita' : models.Food.objects.filter(country_name = '이탈리아'),
	                                    			'event_ita': models.Event.objects.filter(country_name = '이탈리아'),
	                                   				'att_ita' : models.Attraction.objects.filter(country_name='이탈리아'),
	                                   				'food_por' : models.Food.objects.filter(country_name = '포르투갈'),
	                                    			'event_por': models.Event.objects.filter(country_name = '포르투갈'),
	                                   				'att_por' : models.Attraction.objects.filter(country_name='포르투갈'),
	                                   				'food_pol' : models.Food.objects.filter(country_name = '폴란드'),
	                                    			'event_pol': models.Event.objects.filter(country_name = '폴란드'),
	                                   				'att_pol' : models.Attraction.objects.filter(country_name='폴란드'),
	                                   				'food_hun' : models.Food.objects.filter(country_name = '헝가리'),
	                                    			'event_hun': models.Event.objects.filter(country_name = '헝가리'),
	                                   				'att_hun' : models.Attraction.objects.filter(country_name='헝가리'),
													})
	
def result(request):
	global air,depday,arrday,adult_num,kid_num,blue,st,pc,OF,clickOrder2
	adult_num=request.POST.get("adult_num")
	kid_num=request.POST.get("kid_num")
	depday=request.POST.get("depday")
	arrday=request.POST.get("arrday")
	lastcity=request.POST.get("lastcity")
	print(lastcity)
	OF=request.POST.get("order_fix")
	clickOrder=request.POST.get("clickOrder")
	clickOrder2=json.loads(clickOrder)
	print(type(clickOrder2))
	print(clickOrder2[0])
	print(clickOrder2)

	global airport_all
	airport_all=['ICN','FCO','CDG','LHR','MAD','SXF','BRU','FRA','MUC','AMS','DUB','KRK','WAW','BOJ','SOF','NCE','BUD','PRG','LIS','OTP','ZRH','BCN']
	airports = []
	for i in airport_all:
		airports.extend([request.POST.get(i)])

	staytimes= ['stfco','stcdg','stlhr','stmad','stsxf','stbru','stfra','stmuc','stams','stdub','stkrk','stwaw','stboj','stsof','stnce','stbud','stprg','stlis','stotp','stzrh','stbcn']
	staytime = [0]
	for i in staytimes:
		staytime.extend([request.POST.get(i)])
	print(staytime)


	blue=request.POST.get("blue")
	st=request.POST.get("st")
	pc=request.POST.get("pc")
	
	alpha = int(pc)
	beta = int(st)
	print('dd',alpha, beta)
	air=['ICN']
	for airport in clickOrder2:
		air.append(str(airport))
	print(air)

	global special_date, specialdays
	specialdays = ['sdfco','sdcdg','sdlhr','sdmad','sdsxf','sdbru','sdfra','sdmuc','sdams','sddub','sdkrk','sdwaw','sdboj','sdsof','sdnce','sdbud','sdprg','sdlis','sdotp','sdzrh','sdbcn']
	special_date = []
	for i in air:
		ds=request.POST.get(specialdays[airport_all.index(i)-1])
		if ds != '':
			special_date.extend([str(ds)])
		else :
			special_date.extend(['None'])
	print(special_date)
	global lastcity
	if lastcity != "상관없음":
		lastcity = air.index(lastcity)
	else:
		lastcity=100
	print(lastcity)

	global result_air, result_st, result_dep
	result_st = []
	result_air=[]
	result_dep=[]
	global ST
	ST=[]
	for i in air:
   		ST.append(int(str(staytime[airport_all.index(i)])))
   	print('ST',ST)

   	global order_fix
	order_fix=request.POST.get("order_fix")
	print(order_fix)

	if order_fix != None:
		print('YES')
		air_dest = air[1:]
		air_dest.append('ICN')
		order(air,depday,arrday,result_st,result_air,result_dep,alpha,beta,ST,alpha,beta)
	else:
		deftsp(air,depday,arrday,result_st,result_air,result_dep,alpha,beta,ST,lastcity,special_date)
	
	if len(result_st) < 1:
		return render(request, 'pages/mainerror.html')

	global result_air1,result_air2,result_air3
	print("new",result_air)
	result_air1=result_air[:(len(result_air)-1)]
	result_air2=result_air[1:]
	result_air3=result_air[1:(len(result_air)-1)]
	list_num=len(result_air3)
	print(result_air1)
	real_air = []
	real_air = zip(result_air1,result_air2,result_dep)

	print(real_air)
	global real_air

	response = [0]*(len(result_dep))
	api_key= [0]*(len(result_dep))
	url=[0]*(len(result_dep))
	headers=[0]*(len(result_dep))
	params=[0]*(len(result_dep))
	#api_key = "AIzaSyDbpKpdqdIlItEhipc0j6fATk4iHaWdzUw"
	api_key = "AIzaSyDiYhxOy8UR29FtgCQHsZz_7yxRkIrVK_E"
	url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
	headers = {'content-type': 'application/json'}
	global prices
	prices=[]
	stops=[]
	carriers=[]
	carriers_2=[]
	arrivaltimes = []
	departuretimes = []
	durations = []
	second_arrivaltimes=[]
	second_departuretimes = []
	second_durations = []
	second_carriers = []
	layovers = []

	for i in range(len(result_dep)):
		params = {
			"request": {
					"slice": [
						{
						"origin": result_air[i],
						"destination": result_air[i+1],
						"date": result_dep[i],
						"maxStops": 1,
						# "maxConnectionDuration": 5000,
					}
				],
				"passengers": {
					"adultCount": adult_num,
					"childCount": kid_num,
				},
				"solutions": 30,
				# "refundable": False,
				"saleCountry": "US",
			}
		}
		response = requests.post(url, data=json.dumps(params), headers=headers)
		data = response.json()

		price = [0]*3
		stop = [0]*3
		Carrier = [0]*3
		Carriersss = [0]*3
		arrivaltime = [0]*3
		departuretime = [0]*3
		duration = [0]*3
		second_arrivaltime=[0]*3
		second_departuretime = [0]*3
		second_duration = [0]*3
		layover = [0]*3
		durationhour = [0]*3
		durationminute = [0]*3
		second_durationhour = [0]*3
		second_durationminute = [0]*3
		stophour = [0]*3
		stopminute = [0]*3
		second_carrier = [0]*3
		for j in range(3):
			price[j] = data["trips"]["tripOption"][j]["saleTotal"]
			stop[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0].get("connectionDuration", 20000)
			if stop[j] != 20000:	
				second_arrivaltime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["arrivalTime"]
				second_departuretime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["departureTime"]
				second_duration[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["duration"]
				second_carrier[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["flight"]["carrier"]+data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["flight"]["number"]
				layover[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["destination"]
		
			else:
				second_arrivaltime[j] = 0
				second_departuretime[j] = 0
				second_duration[j] = 0
				second_carrier[j] = 0
				layover[j] = 0

			Carrier[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["flight"]["carrier"]+data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["flight"]["number"]
			Carriersss[j]= data["trips"]["data"]["carrier"][j]["name"]
			arrivaltime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["arrivalTime"]
			if int(arrivaltime[j][11:13])< 12 :
			    t=arrivaltime[j][11:13]+':' +arrivaltime[j][14:16]+' AM'

			elif int(arrivaltime[j][11:13])== 13 :
			    t=arrivaltime[j][11:13]+':' +arrivaltime[j][14:16]+' PM'    

			else :
				t='0'+str(int(arrivaltime[j][11:13])-12)+':' +arrivaltime[j][14:16]+' PM'
			arrivaltime[j]= arrivaltime[j][:4]+'년'+' '+arrivaltime[j][5:7]+'월'+' '+arrivaltime[j][8:10]+'일'+' '+t

			departuretime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["departureTime"]
			if int(departuretime[j][11:13])< 12 :
			    print(departuretime[j][11:13])
			    t=departuretime[j][11:13]+':' +departuretime[j][14:16]+' AM'

			elif int(departuretime[j][11:13])== 13 :
			    print(departuretime[j][11:13])
			    t=departuretime[j][11:13]+':' +departuretime[j][14:16]+' PM' 

			else :
				t='0'+str(int(departuretime[j][11:13])-12)+':' +departuretime[j][14:16]+' PM'
			departuretime[j]= departuretime[j][:4]+'년'+' '+departuretime[j][5:7]+'월'+' '+departuretime[j][8:10]+'일'+' '+t

			if stop[j] != 20000:
				if int(second_arrivaltime[j][11:13])< 12 :
				    t=second_arrivaltime[j][11:13]+':' +second_arrivaltime[j][14:16]+' AM'

				elif int(second_arrivaltime[j][11:13])== 13 :
				    t=second_arrivaltime[j][11:13]+':' +second_arrivaltime[j][14:16]+' PM'       

				else :
					t='0'+str(int(second_arrivaltime[j][11:13])-12)+':' +second_arrivaltime[j][14:16]+' PM'
				second_arrivaltime[j] = second_arrivaltime[j][:4]+'년'+' '+second_arrivaltime[j][5:7]+'월'+' '+second_arrivaltime[j][8:10]+'일'+' '+t

				if int(second_departuretime[j][11:13])< 12 :
				    print(second_departuretime[j][11:13])
				    t=second_departuretime[j][11:13]+':' +second_departuretime[j][14:16]+' AM'

				elif int(second_departuretime[j][11:13])== 13 :
				    print(second_departuretime[j][11:13])
				    t=second_departuretime[j][11:13]+':' +second_departuretime[j][14:16]+' PM'

				else :
					t='0'+str(int(second_departuretime[j][11:13])-12)+':' +second_departuretime[j][14:16]+' PM'
				second_departuretime[j]= second_departuretime[j][:4]+'년'+' '+second_departuretime[j][5:7]+'월'+' '+second_departuretime[j][8:10]+'일'+' '+t
				
			

			duration[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]

			durationhour[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]//60
			durationminute[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]%60
			if durationhour[j] < 10:
				durationhour[j]=str(0)+str(durationhour[j])
			if durationminute[j] < 10:
				durationminute[j] = str(0) + str(durationminute[j])
			duration[j] = str(durationhour[j])+"시간 "+str(durationminute[j])+"분 "

			second_durationhour[j] = second_duration[j]//60
			second_durationminute[j] = second_duration[j]%60
			if second_durationhour[j] < 10:
				durationhour[j]=str(0)+str(second_durationhour[j])
			if second_durationminute[j] < 10:
				second_durationminute[j] = str(0) + str(second_durationminute[j])
			second_duration[j] = str(second_durationhour[j])+"시간 "+str(second_durationminute[j])+"분 "

			if stop[j] != 20000:
				stophour[j] = stop[j]//60
				stopminute[j] =stop[j]%60
				if stophour[j] < 10:
					stophour[j]=str(0)+str(stophour[j])
				if stopminute[j] < 10:
					stopminute[j] = str(0) + str(stopminute[j])
				stop[j] = " "+str(stophour[j])+"시간 "+str(stopminute[j])+"분 "

				print(stop)

			prices.append(str(price[j]))
			stops.append(stop[j])
			carriers.append(Carrier[j])
			carriers_2.append(Carriersss[j])
			arrivaltimes.append(arrivaltime[j])
			departuretimes.append(departuretime[j])
			durations.append(duration[j])
			second_arrivaltimes.append(second_arrivaltime[j])
			second_departuretimes.append(second_departuretime[j])
			second_durations.append(second_duration[j])
			second_carriers.append(second_carrier[j])
			layovers.append(layover[j])

	real_price =[]	
	real_stop =[]
	real_carrier =[]
	real_carrier2 =[]
	real_arrivaltime = []
	real_departuretime = []
	real_duration = []
	real_radio=[]
	real_second_arrivaltime = []
	real_second_departuretime= []
	real_second_duration = []
	real_second_carrier = []
	real_layover = []
	for i in range(24):
		real_price.append(str("price")+str(i))
		real_stop.append(str("stop")+str(i))
		real_carrier.append(str("carrier")+str(i))
		real_carrier2.append(str("carrier2_")+str(i))
		real_arrivaltime.append(str("arrivaltime")+str(i))
		real_departuretime.append(str("departuretime")+str(i))
		real_duration.append(str("duration")+str(i))
		real_second_arrivaltime.append(str("second_arrivaltime")+str(i))
		real_second_departuretime.append(str("second_departuretime")+str(i))
		real_second_duration.append(str("second_duration")+str(i))
		real_second_carrier.append(str("second_carrier")+str(i))
		real_layover.append(str("layover")+str(i))

	for i in range(32):	
		real_radio.append(str("radio")+str(i))	



    
	for i in range(len(real_price)-len(prices)):
		prices.append(0)
		stops.append(0)
		carriers.append(0)
		carriers_2.append(0)
		arrivaltimes.append(0)
		departuretimes.append(0)
		durations.append(0)
		second_arrivaltimes.append(0)
		second_departuretimes.append(0)
		second_durations.append(0)
		second_carriers.append(0)
		layovers.append(0)

	radios=[]    
	for i in range(8):
		radios.append(str("radio")+str(i))
	radios=radios*4
	radios.sort()

	for i in zip(real_radio,radios):	
		globals()[i[0]]=i[1]


	for i in zip(real_price,prices,real_stop,stops,real_carrier,carriers,real_carrier2,carriers_2,real_arrivaltime,arrivaltimes,real_departuretime,departuretimes,real_duration,durations,real_second_arrivaltime,second_arrivaltimes,real_second_departuretime,second_departuretimes,real_second_duration,second_durations,real_second_carrier,second_carriers,real_layover,layovers):
		if i[1] != 0:
			globals()[i[0]]=float(i[1][3:])
			globals()[i[2]]=i[3]
			globals()[i[4]]=i[5]
			globals()[i[6]]=i[7]
			globals()[i[8]]=i[9]
			globals()[i[10]]=i[11]
			globals()[i[12]]=i[13]
			globals()[i[14]]=i[15]
			globals()[i[16]]=i[17]
			globals()[i[18]]=i[19]
			globals()[i[20]]=i[21]
			globals()[i[22]]=i[23]
		else:
			globals()[i[0]]=i[1]
			globals()[i[2]]=i[3]
			globals()[i[4]]=i[5]
			globals()[i[6]]=i[7]
			globals()[i[8]]=i[9]
			globals()[i[10]]=i[11]
			globals()[i[12]]=i[13]
			globals()[i[14]]=i[15]
			globals()[i[16]]=i[17]
			globals()[i[18]]=i[19]
			globals()[i[20]]=i[21]
			globals()[i[22]]=i[23]

	conn = sqlite3.connect("lapistadb.db")
	eurail_cost = []
	eurail_dep = []
	eurail_arr = []
	eurail_time = []
	e_dep_date = []
	for i in range(len(result_air) - 1):
		cursor3 = conn.execute(
			"SELECT PRICE,DEP_TIME,ARR_TIME,REQUIRED_TIME from eurail where dep_date=(?) and r_origin=(?) and r_dest=(?)",
			(result_dep[i], result_air[i], result_air[i + 1]))
		eurail_cost.append([])
		eurail_dep.append([])
		eurail_arr.append([])
		eurail_time.append([])
		e_dep_date.append(result_dep[i])
		for row in cursor3:
			eurail_cost[i].append(row[0])
			eurail_dep[i].append(row[1])
			eurail_arr[i].append(row[2])
			eurail_time[i].append(row[3])
		else:
			eurail_cost[i].append(0)
			eurail_dep[i].append(0)
			eurail_arr[i].append(0)
			eurail_time[i].append(0)
	while len(e_dep_date) != 8:
		e_dep_date.append(0)	

	eurail_top_c = [0] * 8
	for i in range(len(eurail_cost)):
		for j in range(len(eurail_cost[i])):
			eurail_top_c[i] = eurail_cost[i][0]

	eurail_top_d = [0] * 8
	for i in range(len(eurail_dep)):
		for j in range(len(eurail_dep[i])):
			eurail_top_d[i] = eurail_dep[i][0]

	eurail_top_a = [0] * 8
	for i in range(len(eurail_arr)):
		for j in range(len(eurail_arr[i])):
			eurail_top_a[i] = eurail_arr[i][0]

	eurail_top_t = [0] * 8
	for i in range(len(eurail_time)):
		for j in range(len(eurail_time[i])):
			eurail_top_t[i] = eurail_time[i][0]

	eurail_info = ['---------------유레일스케쥴--------------'] * 8
	for i in range(len(eurail_cost)):
		for j in range(len(eurail_cost[i])):
			if eurail_cost[i][j] != 0:
				a = '-------$' + str(eurail_cost[i][j]) + ' ' + str(eurail_dep[i][j]) + ' ' + str(eurail_time[i][j]) + '--------'
				eurail_info[i] = ''.join((eurail_info[i], a))
	print(eurail_info)

	Eurail = 'Eurail'
	price_t1=[22,34,55]
	price_t2=0
	E_di = 30000
	prices1=[price0,price1,price2,eurail_top_c[0]]
	prices2=[price3,price4,price5,eurail_top_c[1]]
	prices3=[price6,price7,price8,eurail_top_c[2]]
	prices4=[price9,price10,price11,eurail_top_c[3]]
	prices5=[price12,price13,price14,eurail_top_c[4]]
	prices6=[price15,price16,price17,eurail_top_c[5]]
	prices7=[price18,price19,price20,eurail_top_c[6]]
	prices8=[price21,price22,price23,eurail_top_c[7]]
	global price_all
	price_all=[prices1,prices2,prices3,prices4,prices5,prices6,prices7,prices8]
	stops1=[stop0,stop1,stop2,E_di]
	stops2=[stop3,stop4,stop5,E_di]
	stops3=[stop6,stop7,stop8,E_di]
	stops4=[stop9,stop10,stop11,E_di]
	stops5=[stop12,stop13,stop14,E_di]
	stops6=[stop15,stop16,stop17,E_di]
	stops7=[stop18,stop19,stop20,E_di]
	stops8=[stop21,stop22,stop23,E_di]
	carriers1=[carrier0,carrier1,carrier2,Eurail]
	carriers2=[carrier3,carrier4,carrier5,Eurail]
	carriers3=[carrier6,carrier7,carrier8,Eurail]
	carriers4=[carrier9,carrier10,carrier11,Eurail]
	carriers5=[carrier12,carrier13,carrier14,Eurail]
	carriers6=[carrier15,carrier16,carrier17,Eurail]
	carriers7=[carrier18,carrier19,carrier20,Eurail]
	carriers8=[carrier21,carrier22,carrier23,Eurail]
	carriers2_1=[carrier2_0,carrier2_1,carrier2_2,Eurail]
	carriers2_2=[carrier2_3,carrier2_4,carrier2_5,Eurail]
	carriers2_3=[carrier2_6,carrier2_7,carrier2_8,Eurail]
	carriers2_4=[carrier2_9,carrier2_10,carrier2_11,Eurail]
	carriers2_5=[carrier2_12,carrier2_13,carrier2_14,Eurail]
	carriers2_6=[carrier2_15,carrier2_16,carrier2_17,Eurail]
	carriers2_7=[carrier2_18,carrier2_19,carrier2_20,Eurail]
	carriers2_8=[carrier2_21,carrier2_22,carrier2_23,Eurail]
	arrivaltimes1=[arrivaltime0,arrivaltime1,arrivaltime2,eurail_top_a[0]]
	arrivaltimes2=[arrivaltime3,arrivaltime4,arrivaltime5,eurail_top_a[1]]
	arrivaltimes3=[arrivaltime6,arrivaltime7,arrivaltime8,eurail_top_a[2]]
	arrivaltimes4=[arrivaltime9,arrivaltime10,arrivaltime11,eurail_top_a[3]]
	arrivaltimes5=[arrivaltime12,arrivaltime13,arrivaltime14,eurail_top_a[4]]
	arrivaltimes6=[arrivaltime15,arrivaltime16,arrivaltime17,eurail_top_a[5]]
	arrivaltimes7=[arrivaltime18,arrivaltime19,arrivaltime20,eurail_top_a[6]]
	arrivaltimes8=[arrivaltime21,arrivaltime22,arrivaltime23,eurail_top_a[7]]
	departuretimes1=[departuretime0,departuretime1,departuretime2,e_dep_date[0]]
	departuretimes2=[departuretime3,departuretime4,departuretime5,e_dep_date[1]]
	departuretimes3=[departuretime6,departuretime7,departuretime8,e_dep_date[2]]
	departuretimes4=[departuretime9,departuretime10,departuretime11,e_dep_date[3]]
	departuretimes5=[departuretime12,departuretime13,departuretime14,e_dep_date[4]]
	departuretimes6=[departuretime15,departuretime16,departuretime17,e_dep_date[5]]
	departuretimes7=[departuretime18,departuretime19,departuretime20,e_dep_date[6]]
	departuretimes8=[departuretime21,departuretime22,departuretime23,e_dep_date[7]]
	durations1=[duration0,duration1,duration2,eurail_top_t[0]]
	durations2=[duration3,duration4,duration5,eurail_top_t[1]]
	durations3=[duration6,duration7,duration8,eurail_top_t[2]]
	durations4=[duration9,duration10,duration11,eurail_top_t[3]]
	durations5=[duration12,duration13,duration14,eurail_top_t[4]]
	durations6=[duration15,duration16,duration17,eurail_top_t[5]]
	durations7=[duration18,duration19,duration20,eurail_top_t[6]]
	durations8=[duration21,duration22,duration23,eurail_top_t[7]]
	radios1=[radio0,radio1,radio2,radio3]
	radios2=[radio4,radio5,radio6,radio7]
	radios3=[radio8,radio9,radio10,radio11]
	radios4=[radio12,radio13,radio14,radio15]
	radios5=[radio16,radio17,radio18,radio19]
	radios6=[radio20,radio21,radio22,radio23]
	radios7=[radio24,radio25,radio26,radio27]
	radios8=[radio28,radio29,radio30,radio31]
	second_arrivaltimes1=[second_arrivaltime0,second_arrivaltime1,second_arrivaltime2,price_t2]
	second_arrivaltimes2=[second_arrivaltime3,second_arrivaltime4,second_arrivaltime5,price_t2]
	second_arrivaltimes3=[second_arrivaltime6,second_arrivaltime7,second_arrivaltime8,price_t2]
	second_arrivaltimes4=[second_arrivaltime9,second_arrivaltime10,second_arrivaltime11,price_t2]
	second_arrivaltimes5=[second_arrivaltime12,second_arrivaltime13,second_arrivaltime14,price_t2]
	second_arrivaltimes6=[second_arrivaltime15,second_arrivaltime16,second_arrivaltime17,price_t2]
	second_arrivaltimes7=[second_arrivaltime18,second_arrivaltime19,second_arrivaltime20,price_t2]
	second_arrivaltimes8=[second_arrivaltime21,second_arrivaltime22,second_arrivaltime23,price_t2]
	second_departuretimes1=[second_departuretime0,second_departuretime1,second_departuretime2,price_t2]
	second_departuretimes2=[second_departuretime3,second_departuretime4,second_departuretime5,price_t2]
	second_departuretimes3=[second_departuretime6,second_departuretime7,second_departuretime8,price_t2]
	second_departuretimes4=[second_departuretime9,second_departuretime10,second_departuretime11,price_t2]
	second_departuretimes5=[second_departuretime12,second_departuretime13,second_departuretime14,price_t2]
	second_departuretimes6=[second_departuretime15,second_departuretime16,second_departuretime17,price_t2]
	second_departuretimes7=[second_departuretime18,second_departuretime19,second_departuretime20,price_t2]
	second_departuretimes8=[second_departuretime21,second_departuretime22,second_departuretime23,price_t2]
	second_durations1=[second_duration0,second_duration1,second_duration2,price_t2]
	second_durations2=[second_duration3,second_duration4,second_duration5,price_t2]
	second_durations3=[second_duration6,second_duration7,second_duration8,price_t2]
	second_durations4=[second_duration9,second_duration10,second_duration11,price_t2]
	second_durations5=[second_duration12,second_duration13,second_duration14,price_t2]
	second_durations6=[second_duration15,second_duration16,second_duration17,price_t2]
	second_durations7=[second_duration18,second_duration19,second_duration20,price_t2]
	second_durations8=[second_duration21,second_duration22,second_duration23,price_t2]
	second_carriers1=[second_carrier0,second_carrier1,second_carrier2,price_t1]
	second_carriers2=[second_carrier3,second_carrier4,second_carrier5,price_t1]
	second_carriers3=[second_carrier6,second_carrier7,second_carrier8,price_t1]
	second_carriers4=[second_carrier9,second_carrier10,second_carrier11,price_t1]
	second_carriers5=[second_carrier12,second_carrier13,second_carrier14,price_t1]
	second_carriers6=[second_carrier15,second_carrier16,second_carrier17,price_t1]
	second_carriers7=[second_carrier18,second_carrier19,second_carrier20,price_t1]
	second_carriers8=[second_carrier21,second_carrier22,second_carrier23,price_t1]
	layovers1=[layover0,layover1,layover2,eurail_info[0]]
	layovers2=[layover3,layover4,layover5,eurail_info[1]]
	layovers3=[layover6,layover7,layover8,eurail_info[2]]
	layovers4=[layover9,layover10,layover11,eurail_info[3]]
	layovers5=[layover12,layover13,layover14,eurail_info[4]]
	layovers6=[layover15,layover16,layover17,eurail_info[5]]
	layovers7=[layover18,layover19,layover20,eurail_info[6]]
	layovers8=[layover21,layover22,layover23,eurail_info[7]]

	result_st2=result_st[1:]
	global kkk
	kkk=[zip(prices1,stops1,carriers1,carriers2_1,arrivaltimes1,departuretimes1,durations1,radios1,second_departuretimes1,second_arrivaltimes1,second_durations1,second_carriers1,layovers1),zip(prices2,stops2,carriers2,carriers2_2,arrivaltimes2,departuretimes2,durations2,radios2,second_departuretimes2,second_arrivaltimes2,second_durations2,second_carriers2,layovers2),zip(prices3,stops3,carriers3,carriers2_3,arrivaltimes3,departuretimes3,durations3,radios3,second_departuretimes3,second_arrivaltimes3,second_durations3,second_carriers3,layovers3),zip(prices4,stops4,carriers4,carriers2_4,arrivaltimes4,departuretimes4,durations4,radios4,second_departuretimes4,second_arrivaltimes4,second_durations4,second_carriers4,layovers4),zip(prices5,stops5,carriers5,carriers2_5,arrivaltimes5,departuretimes5,durations5,radios5,second_departuretimes5,second_arrivaltimes5,second_durations5,second_carriers5,layovers5),zip(prices6,stops6,carriers6,carriers2_6,arrivaltimes6,departuretimes6,durations6,radios6,second_departuretimes6,second_arrivaltimes6,second_durations6,second_carriers6,layovers6),zip(prices7,stops7,carriers7,carriers2_7,arrivaltimes7,departuretimes7,durations7,radios7,second_departuretimes7,second_arrivaltimes7,second_durations7,second_carriers7,layovers7),zip(prices8,stops8,carriers8,carriers2_8,arrivaltimes8,departuretimes8,durations8,radios8,second_departuretimes8,second_arrivaltimes8,second_durations8,second_carriers8,layovers8)]

	lhr_loc={}
	lhr_loc['lat']=51.27159
	lhr_loc['lng']=-0.20443
	
	cdg_loc={}
	cdg_loc['lat']=48.646
	cdg_loc['lng']=2.330

	mad_loc={}
	mad_loc['lat']=40.5
	mad_loc['lng']=-3.567

	fco_loc={}
	fco_loc['lat']=41.8
	fco_loc['lng']=12.25

	sxf_loc={}
	sxf_loc['lat']=52.56
	sxf_loc['lng']=13.29

	bru_loc={}
	bru_loc['lat']=50.900755
	bru_loc['lng']=4.479653

	fra_loc={}
	fra_loc['lat']=50.038105
	fra_loc['lng']=8.562474

	muc_loc={}
	muc_loc['lat']=48.358051
	muc_loc['lng']=11.784187

	ams_loc={}
	ams_loc['lat']=52.310834
	ams_loc['lng']=4.768071

	dub_loc={}
	dub_loc['lat']=53.426646
	dub_loc['lng']=-6.250135

	krk_loc={}
	krk_loc['lat']=50.077095
	krk_loc['lng']=19.787271

	waw_loc={}
	waw_loc['lat']=52.167526
	waw_loc['lng']=20.967440

	boj_loc={}
	boj_loc['lat']=42.565492
	boj_loc['lng']=27.516538

	sof_loc={}
	sof_loc['lat']=42.689235
	sof_loc['lng']=23.414747

	nce_loc={}
	nce_loc['lat']=43.660048
	nce_loc['lng']=7.214049

	bud_loc={}
	bud_loc['lat']=47.438604
	bud_loc['lng']=19.251588

	prg_loc={}
	prg_loc['lat']=50.102101
	prg_loc['lng']=14.262849

	lis_loc={}
	lis_loc['lat']=38.775953
	lis_loc['lng']=-9.135495

	otp_loc={}
	otp_loc['lat']=44.571227
	otp_loc['lng']=26.084412

	zrh_loc={}
	zrh_loc['lat']=47.458362
	zrh_loc['lng']=8.554821

	bcn_loc={}
	bcn_loc['lat']=41.297308
	bcn_loc['lng']=2.082811

	global location_all
	location_all=[fco_loc,cdg_loc,lhr_loc,mad_loc,sxf_loc,bru_loc,fra_loc,muc_loc,ams_loc,dub_loc,krk_loc,waw_loc,boj_loc,sof_loc,nce_loc,bud_loc,prg_loc,lis_loc,otp_loc,zrh_loc,bcn_loc]

	global location_real
	location_real=[]
	for i in result_air3:
	   a=airport_all.index(i)
	   location_real.append(location_all[a-1])

	global first_dep
  	c=airport_all.index(result_air3[0])
	first_dep=location_all[c-1]

	global air_result_kor   
	air_result_kor = []
   	for i in result_air3:
		air_kor_name = models.Airport.objects.get(air_name = i)
		air_result_kor.append(air_kor_name.city_name)

	global results2, results3	
	results2=zip(air_result_kor,result_st2)
	results3=zip(air_result_kor,result_st2,result_air3)
	return render(request, 'pages/result.html', {"adult_num": adult_num,
												 "kid_num": kid_num,
												 "depday": depday,
												 "arrday": arrday,
												 "location_real":location_real,
												 "result_air":result_air,
											     "kkk": kkk,
											     "real_air":real_air,
											     "results2":results2,
											     "result_air3":result_air3,
											     "air_result_kor" : air_result_kor,
											     "results3":results3,
											     "lastcity":lastcity,
											     "first_dep":first_dep,
											     "list_num":list_num,
												 })

def staytime(request):
	global result_st, result_dep, result_air
	result_st = []
	result_air=[]
	result_dep=[]

	alpha=1
	beta=5

	if order_fix != None:
		print('YES')
		air_dest = air[1:]
		air_dest.append('ICN')
		order(air,depday,arrday,result_st,result_air,result_dep,alpha,beta,ST,alpha,beta)
	else:
		deftsp(air,depday,arrday,result_st,result_air,result_dep,alpha,beta,ST,lastcity,special_date)
	
	if len(result_st) < 1:
		return render(request, 'pages/mainerror.html')

	global result_air1,result_air2,result_air3
	result_air1=[]
	result_air2=[]
	result_air3=[]
	print("new",result_air)
	result_air1=result_air[:(len(result_air)-1)]
	result_air2=result_air[1:]
	result_air3=result_air[1:(len(result_air)-1)]
	list_num=len(result_air3)
	print(result_air1)
	real_air = []
	real_air = zip(result_air1,result_air2,result_dep)

	print(real_air)
	global real_air

	response = [0]*(len(result_dep))
	api_key= [0]*(len(result_dep))
	url=[0]*(len(result_dep))
	headers=[0]*(len(result_dep))
	params=[0]*(len(result_dep))
	# api_key="AIzaSyDbpKpdqdIlItEhipc0j6fATk4iHaWdzUw"
	api_key = "AIzaSyDiYhxOy8UR29FtgCQHsZz_7yxRkIrVK_E"
	url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
	headers = {'content-type': 'application/json'}
	global prices
	prices=[]
	stops=[]
	carriers=[]
	carriers_2=[]
	arrivaltimes = []
	departuretimes = []
	durations = []
	second_arrivaltimes=[]
	second_departuretimes = []
	second_durations = []
	second_carriers = []
	layovers = []

	for i in range(len(result_dep)):
		params = {
			"request": {
					"slice": [
						{
						"origin": result_air[i],
						"destination": result_air[i+1],
						"date": result_dep[i],
						"maxStops": 1,
						# "maxConnectionDuration": 5000,
					}
				],
				"passengers": {
					"adultCount": adult_num,
					"childCount": kid_num,
				},
				"solutions": 30,
				# "refundable": False,
				"saleCountry": "US",
			}
		}
		response = requests.post(url, data=json.dumps(params), headers=headers)
		data = response.json()

		price = [0]*3
		stop = [0]*3
		Carrier = [0]*3
		Carriersss = [0]*3
		arrivaltime = [0]*3
		departuretime = [0]*3
		duration = [0]*3
		second_arrivaltime=[0]*3
		second_departuretime = [0]*3
		second_duration = [0]*3
		layover = [0]*3
		durationhour = [0]*3
		durationminute = [0]*3
		second_durationhour = [0]*3
		second_durationminute = [0]*3
		stophour = [0]*3
		stopminute = [0]*3
		second_carrier = [0]*3
		for j in range(3):
			price[j] = data["trips"]["tripOption"][j]["saleTotal"]
			stop[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0].get("connectionDuration", 20000)
			if stop[j] != 20000:	
				second_arrivaltime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["arrivalTime"]
				second_departuretime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["departureTime"]
				second_duration[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["duration"]
				second_carrier[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["flight"]["carrier"]+data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["flight"]["number"]
				layover[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["destination"]
		
			else:
				second_arrivaltime[j] = 0
				second_departuretime[j] = 0
				second_duration[j] = 0
				second_carrier[j] = 0
				layover[j] = 0

			Carrier[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["flight"]["carrier"]+data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["flight"]["number"]
			Carriersss[j]= data["trips"]["data"]["carrier"][j]["name"]
			arrivaltime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["arrivalTime"]
			if int(arrivaltime[j][11:13])< 12 :
			    t=arrivaltime[j][11:13]+':' +arrivaltime[j][14:16]+' AM'

			elif int(arrivaltime[j][11:13])== 13 :
			    t=arrivaltime[j][11:13]+':' +arrivaltime[j][14:16]+' PM'     

			else :
				t='0'+str(int(arrivaltime[j][11:13])-12)+':' +arrivaltime[j][14:16]+' PM'
			arrivaltime[j]= arrivaltime[j][:4]+'년'+' '+arrivaltime[j][5:7]+'월'+' '+arrivaltime[j][8:10]+'일'+' '+t

			departuretime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["departureTime"]
			if int(departuretime[j][11:13])< 12 :
			    print(departuretime[j][11:13])
			    t=departuretime[j][11:13]+':' +departuretime[j][14:16]+' AM'

			elif int(departuretime[j][11:13])== 13 :
			    print(departuretime[j][11:13])
			    t=departuretime[j][11:13]+':' +departuretime[j][14:16]+' PM'

			else :
				t='0'+str(int(departuretime[j][11:13])-12)+':' +departuretime[j][14:16]+' PM'
			departuretime[j]= departuretime[j][:4]+'년'+' '+departuretime[j][5:7]+'월'+' '+departuretime[j][8:10]+'일'+' '+t

			if stop[j] != 20000:
				if int(second_arrivaltime[j][11:13])< 12 :
				    t=second_arrivaltime[j][11:13]+':' +second_arrivaltime[j][14:16]+' AM'

				elif int(second_arrivaltime[j][11:13])== 13 :
				    t=second_arrivaltime[j][11:13]+':' +second_arrivaltime[j][14:16]+' PM' 

				else :
					t='0'+str(int(second_arrivaltime[j][11:13])-12)+':' +second_arrivaltime[j][14:16]+' PM'
				second_arrivaltime[j] = second_arrivaltime[j][:4]+'년'+' '+second_arrivaltime[j][5:7]+'월'+' '+second_arrivaltime[j][8:10]+'일'+' '+t

				if int(second_departuretime[j][11:13])< 12 :
				    print(second_departuretime[j][11:13])
				    t=second_departuretime[j][11:13]+':' +second_departuretime[j][14:16]+' AM'

				elif int(second_departuretime[j][11:13])== 13 :
				    print(second_departuretime[j][11:13])
				    t=second_departuretime[j][11:13]+':' +second_departuretime[j][14:16]+' PM'

				else :
					t='0'+str(int(second_departuretime[j][11:13])-12)+':' +second_departuretime[j][14:16]+' PM'
				second_departuretime[j]= second_departuretime[j][:4]+'년'+' '+second_departuretime[j][5:7]+'월'+' '+second_departuretime[j][8:10]+'일'+' '+t
				
			

			duration[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]

			durationhour[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]//60
			durationminute[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]%60
			if durationhour[j] < 10:
				durationhour[j]=str(0)+str(durationhour[j])
			if durationminute[j] < 10:
				durationminute[j] = str(0) + str(durationminute[j])
			duration[j] = str(durationhour[j])+"시간 "+str(durationminute[j])+"분 "

			second_durationhour[j] = second_duration[j]//60
			second_durationminute[j] = second_duration[j]%60
			if second_durationhour[j] < 10:
				durationhour[j]=str(0)+str(second_durationhour[j])
			if second_durationminute[j] < 10:
				second_durationminute[j] = str(0) + str(second_durationminute[j])
			second_duration[j] = str(second_durationhour[j])+"시간 "+str(second_durationminute[j])+"분 "

			if stop[j] != 20000:
				stophour[j] = stop[j]//60
				stopminute[j] =stop[j]%60
				if stophour[j] < 10:
					stophour[j]=str(0)+str(stophour[j])
				if stopminute[j] < 10:
					stopminute[j] = str(0) + str(stopminute[j])
				stop[j] = " "+str(stophour[j])+"시간 "+str(stopminute[j])+"분 "

				print(stop)

			prices.append(str(price[j]))
			stops.append(stop[j])
			carriers.append(Carrier[j])
			carriers_2.append(Carriersss[j])
			arrivaltimes.append(arrivaltime[j])
			departuretimes.append(departuretime[j])
			durations.append(duration[j])
			second_arrivaltimes.append(second_arrivaltime[j])
			second_departuretimes.append(second_departuretime[j])
			second_durations.append(second_duration[j])
			second_carriers.append(second_carrier[j])
			layovers.append(layover[j])

	real_price =[]	
	real_stop =[]
	real_carrier =[]
	real_carrier2 =[]
	real_arrivaltime = []
	real_departuretime = []
	real_duration = []
	real_radio=[]
	real_second_arrivaltime = []
	real_second_departuretime= []
	real_second_duration = []
	real_second_carrier = []
	real_layover = []
	for i in range(24):
		real_price.append(str("price")+str(i))
		real_stop.append(str("stop")+str(i))
		real_carrier.append(str("carrier")+str(i))
		real_carrier2.append(str("carrier2_")+str(i))
		real_arrivaltime.append(str("arrivaltime")+str(i))
		real_departuretime.append(str("departuretime")+str(i))
		real_duration.append(str("duration")+str(i))
		real_second_arrivaltime.append(str("second_arrivaltime")+str(i))
		real_second_departuretime.append(str("second_departuretime")+str(i))
		real_second_duration.append(str("second_duration")+str(i))
		real_second_carrier.append(str("second_carrier")+str(i))
		real_layover.append(str("layover")+str(i))

	for i in range(32):	
		real_radio.append(str("radio")+str(i))	



    
	for i in range(len(real_price)-len(prices)):
		prices.append(0)
		stops.append(0)
		carriers.append(0)
		carriers_2.append(0)
		arrivaltimes.append(0)
		departuretimes.append(0)
		durations.append(0)
		second_arrivaltimes.append(0)
		second_departuretimes.append(0)
		second_durations.append(0)
		second_carriers.append(0)
		layovers.append(0)

	radios=[]    
	for i in range(8):
		radios.append(str("radio")+str(i))
	radios=radios*4
	radios.sort()

	for i in zip(real_radio,radios):	
		globals()[i[0]]=i[1]


	for i in zip(real_price,prices,real_stop,stops,real_carrier,carriers,real_carrier2,carriers_2,real_arrivaltime,arrivaltimes,real_departuretime,departuretimes,real_duration,durations,real_second_arrivaltime,second_arrivaltimes,real_second_departuretime,second_departuretimes,real_second_duration,second_durations,real_second_carrier,second_carriers,real_layover,layovers):
		if i[1] != 0:
			globals()[i[0]]=float(i[1][3:])
			globals()[i[2]]=i[3]
			globals()[i[4]]=i[5]
			globals()[i[6]]=i[7]
			globals()[i[8]]=i[9]
			globals()[i[10]]=i[11]
			globals()[i[12]]=i[13]
			globals()[i[14]]=i[15]
			globals()[i[16]]=i[17]
			globals()[i[18]]=i[19]
			globals()[i[20]]=i[21]
			globals()[i[22]]=i[23]
		else:
			globals()[i[0]]=i[1]
			globals()[i[2]]=i[3]
			globals()[i[4]]=i[5]
			globals()[i[6]]=i[7]
			globals()[i[8]]=i[9]
			globals()[i[10]]=i[11]
			globals()[i[12]]=i[13]
			globals()[i[14]]=i[15]
			globals()[i[16]]=i[17]
			globals()[i[18]]=i[19]
			globals()[i[20]]=i[21]
			globals()[i[22]]=i[23]

	conn = sqlite3.connect("lapistadb.db")
	eurail_cost = []
	eurail_dep = []
	eurail_arr = []
	eurail_time = []
	e_dep_date = []
	for i in range(len(result_air) - 1):
		cursor3 = conn.execute(
			"SELECT PRICE,DEP_TIME,ARR_TIME,REQUIRED_TIME from eurail where dep_date=(?) and r_origin=(?) and r_dest=(?)",
			(result_dep[i], result_air[i], result_air[i + 1]))
		eurail_cost.append([])
		eurail_dep.append([])
		eurail_arr.append([])
		eurail_time.append([])
		e_dep_date.append(result_dep[i])
		for row in cursor3:
			eurail_cost[i].append(row[0])
			eurail_dep[i].append(row[1])
			eurail_arr[i].append(row[2])
			eurail_time[i].append(row[3])
		else:
			eurail_cost[i].append(0)
			eurail_dep[i].append(0)
			eurail_arr[i].append(0)
			eurail_time[i].append(0)

	while len(e_dep_date) != 8:
		e_dep_date.append(0)		

	eurail_top_c = [0] * 8
	for i in range(len(eurail_cost)):
		for j in range(len(eurail_cost[i])):
			eurail_top_c[i] = eurail_cost[i][0]

	eurail_top_d = [0] * 8
	for i in range(len(eurail_dep)):
		for j in range(len(eurail_dep[i])):
			eurail_top_d[i] = eurail_dep[i][0]

	eurail_top_a = [0] * 8
	for i in range(len(eurail_arr)):
		for j in range(len(eurail_arr[i])):
			eurail_top_a[i] = eurail_arr[i][0]

	eurail_top_t = [0] * 8
	for i in range(len(eurail_time)):
		for j in range(len(eurail_time[i])):
			eurail_top_t[i] = eurail_time[i][0]

	eurail_info = ['---------------유레일스케쥴--------------'] * 8
	for i in range(len(eurail_cost)):
		for j in range(len(eurail_cost[i])):
			if eurail_cost[i][j] != 0:
				a = '-------$' + str(eurail_cost[i][j]) + ' ' + str(eurail_dep[i][j]) + ' ' + str(eurail_time[i][j]) + '--------'
				eurail_info[i] = ''.join((eurail_info[i], a))
	print(eurail_info)

	Eurail = 'Eurail'
	price_t1=[22,34,55]
	price_t2=0
	E_di = 30000
	prices1=[price0,price1,price2,eurail_top_c[0]]
	prices2=[price3,price4,price5,eurail_top_c[1]]
	prices3=[price6,price7,price8,eurail_top_c[2]]
	prices4=[price9,price10,price11,eurail_top_c[3]]
	prices5=[price12,price13,price14,eurail_top_c[4]]
	prices6=[price15,price16,price17,eurail_top_c[5]]
	prices7=[price18,price19,price20,eurail_top_c[6]]
	prices8=[price21,price22,price23,eurail_top_c[7]]
	global price_all
	price_all=[]
	price_all=[prices1,prices2,prices3,prices4,prices5,prices6,prices7,prices8]
	stops1=[stop0,stop1,stop2,E_di]
	stops2=[stop3,stop4,stop5,E_di]
	stops3=[stop6,stop7,stop8,E_di]
	stops4=[stop9,stop10,stop11,E_di]
	stops5=[stop12,stop13,stop14,E_di]
	stops6=[stop15,stop16,stop17,E_di]
	stops7=[stop18,stop19,stop20,E_di]
	stops8=[stop21,stop22,stop23,E_di]
	carriers1=[carrier0,carrier1,carrier2,Eurail]
	carriers2=[carrier3,carrier4,carrier5,Eurail]
	carriers3=[carrier6,carrier7,carrier8,Eurail]
	carriers4=[carrier9,carrier10,carrier11,Eurail]
	carriers5=[carrier12,carrier13,carrier14,Eurail]
	carriers6=[carrier15,carrier16,carrier17,Eurail]
	carriers7=[carrier18,carrier19,carrier20,Eurail]
	carriers8=[carrier21,carrier22,carrier23,Eurail]
	carriers2_1=[carrier2_0,carrier2_1,carrier2_2,Eurail]
	carriers2_2=[carrier2_3,carrier2_4,carrier2_5,Eurail]
	carriers2_3=[carrier2_6,carrier2_7,carrier2_8,Eurail]
	carriers2_4=[carrier2_9,carrier2_10,carrier2_11,Eurail]
	carriers2_5=[carrier2_12,carrier2_13,carrier2_14,Eurail]
	carriers2_6=[carrier2_15,carrier2_16,carrier2_17,Eurail]
	carriers2_7=[carrier2_18,carrier2_19,carrier2_20,Eurail]
	carriers2_8=[carrier2_21,carrier2_22,carrier2_23,Eurail]
	arrivaltimes1=[arrivaltime0,arrivaltime1,arrivaltime2,eurail_top_a[0]]
	arrivaltimes2=[arrivaltime3,arrivaltime4,arrivaltime5,eurail_top_a[1]]
	arrivaltimes3=[arrivaltime6,arrivaltime7,arrivaltime8,eurail_top_a[2]]
	arrivaltimes4=[arrivaltime9,arrivaltime10,arrivaltime11,eurail_top_a[3]]
	arrivaltimes5=[arrivaltime12,arrivaltime13,arrivaltime14,eurail_top_a[4]]
	arrivaltimes6=[arrivaltime15,arrivaltime16,arrivaltime17,eurail_top_a[5]]
	arrivaltimes7=[arrivaltime18,arrivaltime19,arrivaltime20,eurail_top_a[6]]
	arrivaltimes8=[arrivaltime21,arrivaltime22,arrivaltime23,eurail_top_a[7]]
	departuretimes1=[departuretime0,departuretime1,departuretime2,e_dep_date[0]]
	departuretimes2=[departuretime3,departuretime4,departuretime5,e_dep_date[1]]
	departuretimes3=[departuretime6,departuretime7,departuretime8,e_dep_date[2]]
	departuretimes4=[departuretime9,departuretime10,departuretime11,e_dep_date[3]]
	departuretimes5=[departuretime12,departuretime13,departuretime14,e_dep_date[4]]
	departuretimes6=[departuretime15,departuretime16,departuretime17,e_dep_date[5]]
	departuretimes7=[departuretime18,departuretime19,departuretime20,e_dep_date[6]]
	departuretimes8=[departuretime21,departuretime22,departuretime23,e_dep_date[7]]
	durations1=[duration0,duration1,duration2,eurail_top_t[0]]
	durations2=[duration3,duration4,duration5,eurail_top_t[1]]
	durations3=[duration6,duration7,duration8,eurail_top_t[2]]
	durations4=[duration9,duration10,duration11,eurail_top_t[3]]
	durations5=[duration12,duration13,duration14,eurail_top_t[4]]
	durations6=[duration15,duration16,duration17,eurail_top_t[5]]
	durations7=[duration18,duration19,duration20,eurail_top_t[6]]
	durations8=[duration21,duration22,duration23,eurail_top_t[7]]
	radios1=[radio0,radio1,radio2,radio3]
	radios2=[radio4,radio5,radio6,radio7]
	radios3=[radio8,radio9,radio10,radio11]
	radios4=[radio12,radio13,radio14,radio15]
	radios5=[radio16,radio17,radio18,radio19]
	radios6=[radio20,radio21,radio22,radio23]
	radios7=[radio24,radio25,radio26,radio27]
	radios8=[radio28,radio29,radio30,radio31]
	second_arrivaltimes1=[second_arrivaltime0,second_arrivaltime1,second_arrivaltime2,price_t1]
	second_arrivaltimes2=[second_arrivaltime3,second_arrivaltime4,second_arrivaltime5,price_t1]
	second_arrivaltimes3=[second_arrivaltime6,second_arrivaltime7,second_arrivaltime8,price_t1]
	second_arrivaltimes4=[second_arrivaltime9,second_arrivaltime10,second_arrivaltime11,price_t2]
	second_arrivaltimes5=[second_arrivaltime12,second_arrivaltime13,second_arrivaltime14,price_t2]
	second_arrivaltimes6=[second_arrivaltime15,second_arrivaltime16,second_arrivaltime17,price_t2]
	second_arrivaltimes7=[second_arrivaltime18,second_arrivaltime19,second_arrivaltime20,price_t2]
	second_arrivaltimes8=[second_arrivaltime21,second_arrivaltime22,second_arrivaltime23,price_t2]
	second_departuretimes1=[second_departuretime0,second_departuretime1,second_departuretime2,price_t1]
	second_departuretimes2=[second_departuretime3,second_departuretime4,second_departuretime5,price_t1]
	second_departuretimes3=[second_departuretime6,second_departuretime7,second_departuretime8,price_t1]
	second_departuretimes4=[second_departuretime9,second_departuretime10,second_departuretime11,price_t2]
	second_departuretimes5=[second_departuretime12,second_departuretime13,second_departuretime14,price_t2]
	second_departuretimes6=[second_departuretime15,second_departuretime16,second_departuretime17,price_t2]
	second_departuretimes7=[second_departuretime18,second_departuretime19,second_departuretime20,price_t2]
	second_departuretimes8=[second_departuretime21,second_departuretime22,second_departuretime23,price_t2]
	second_durations1=[second_duration0,second_duration1,second_duration2,price_t1]
	second_durations2=[second_duration3,second_duration4,second_duration5,price_t1]
	second_durations3=[second_duration6,second_duration7,second_duration8,price_t1]
	second_durations4=[second_duration9,second_duration10,second_duration11,price_t2]
	second_durations5=[second_duration12,second_duration13,second_duration14,price_t2]
	second_durations6=[second_duration15,second_duration16,second_duration17,price_t2]
	second_durations7=[second_duration18,second_duration19,second_duration20,price_t2]
	second_durations8=[second_duration21,second_duration22,second_duration23,price_t2]
	second_carriers1=[second_carrier0,second_carrier1,second_carrier2,price_t1]
	second_carriers2=[second_carrier3,second_carrier4,second_carrier5,price_t1]
	second_carriers3=[second_carrier6,second_carrier7,second_carrier8,price_t1]
	second_carriers4=[second_carrier9,second_carrier10,second_carrier11,price_t1]
	second_carriers5=[second_carrier12,second_carrier13,second_carrier14,price_t1]
	second_carriers6=[second_carrier15,second_carrier16,second_carrier17,price_t1]
	second_carriers7=[second_carrier18,second_carrier19,second_carrier20,price_t1]
	second_carriers8=[second_carrier21,second_carrier22,second_carrier23,price_t1]
	layovers1=[layover0,layover1,layover2,eurail_info[0]]
	layovers2=[layover3,layover4,layover5,eurail_info[1]]
	layovers3=[layover6,layover7,layover8,eurail_info[2]]
	layovers4=[layover9,layover10,layover11,eurail_info[3]]
	layovers5=[layover12,layover13,layover14,eurail_info[4]]
	layovers6=[layover15,layover16,layover17,eurail_info[5]]
	layovers7=[layover18,layover19,layover20,eurail_info[6]]
	layovers8=[layover21,layover22,layover23,eurail_info[7]]

	result_st2=result_st[1:]
	global kkk
	kkk=[]
	kkk=[zip(prices1,stops1,carriers1,carriers2_1,arrivaltimes1,departuretimes1,durations1,radios1,second_departuretimes1,second_arrivaltimes1,second_durations1,second_carriers1,layovers1),zip(prices2,stops2,carriers2,carriers2_2,arrivaltimes2,departuretimes2,durations2,radios2,second_departuretimes2,second_arrivaltimes2,second_durations2,second_carriers2,layovers2),zip(prices3,stops3,carriers3,carriers2_3,arrivaltimes3,departuretimes3,durations3,radios3,second_departuretimes3,second_arrivaltimes3,second_durations3,second_carriers3,layovers3),zip(prices4,stops4,carriers4,carriers2_4,arrivaltimes4,departuretimes4,durations4,radios4,second_departuretimes4,second_arrivaltimes4,second_durations4,second_carriers4,layovers4),zip(prices5,stops5,carriers5,carriers2_5,arrivaltimes5,departuretimes5,durations5,radios5,second_departuretimes5,second_arrivaltimes5,second_durations5,second_carriers5,layovers5),zip(prices6,stops6,carriers6,carriers2_6,arrivaltimes6,departuretimes6,durations6,radios6,second_departuretimes6,second_arrivaltimes6,second_durations6,second_carriers6,layovers6),zip(prices7,stops7,carriers7,carriers2_7,arrivaltimes7,departuretimes7,durations7,radios7,second_departuretimes7,second_arrivaltimes7,second_durations7,second_carriers7,layovers7),zip(prices8,stops8,carriers8,carriers2_8,arrivaltimes8,departuretimes8,durations8,radios8,second_departuretimes8,second_arrivaltimes8,second_durations8,second_carriers8,layovers8)]

	global location_real
	location_real=[]
	for i in result_air3:
	   a=airport_all.index(i)
	   location_real.append(location_all[a-1])

	global first_dep
	first_dep=[]
  	c=airport_all.index(result_air3[0])
	first_dep=location_all[c-1]

	global air_result_kor   
	air_result_kor = []
   	for i in result_air3:
		air_kor_name = models.Airport.objects.get(air_name = i)
		air_result_kor.append(air_kor_name.city_name)

	global results2, results3
	results2=[]
	results3=[]	
	results2=zip(air_result_kor,result_st2)
	results3=zip(air_result_kor,result_st2,result_air3)

	return render(request, 'pages/staytime.html',  {"adult_num": adult_num,
												 	"kid_num": kid_num,
												 	"depday": depday,
												 	"arrday": arrday,
												 	"location_real":location_real,
												 	"result_air":result_air,
											     	"kkk": kkk,
											     	"real_air":real_air,
											     	"results2":results2,
											     	"result_air3":result_air3,
											     	"air_result_kor" : air_result_kor,
											     	"results3":results3,
											     	"lastcity":lastcity,
											     	"first_dep":first_dep,
												    })
def price(request):
	global result_st, result_dep, result_air
	result_st = []
	result_air=[]
	result_dep=[]

	alpha=10
	beta=1

	if order_fix != None:
		print('YES')
		air_dest = air[1:]
		air_dest.append('ICN')
		order(air,depday,arrday,result_st,result_air,result_dep,alpha,beta,ST,alpha,beta)
	else:
		deftsp(air,depday,arrday,result_st,result_air,result_dep,alpha,beta,ST,lastcity,special_date)
	
	if len(result_st) < 1:
		return render(request, 'pages/mainerror.html')

	global result_air1,result_air2,result_air3
	result_air1=[]
	result_air2=[]
	result_air3=[]
	print("new",result_air)
	result_air1=result_air[:(len(result_air)-1)]
	result_air2=result_air[1:]
	result_air3=result_air[1:(len(result_air)-1)]
	list_num=len(result_air3)
	print(result_air1)
	real_air = []
	real_air = zip(result_air1,result_air2,result_dep)

	print(real_air)
	global real_air

	response = [0]*(len(result_dep))
	api_key= [0]*(len(result_dep))
	url=[0]*(len(result_dep))
	headers=[0]*(len(result_dep))
	params=[0]*(len(result_dep))
	# api_key="AIzaSyDbpKpdqdIlItEhipc0j6fATk4iHaWdzUw"
	api_key = "AIzaSyDiYhxOy8UR29FtgCQHsZz_7yxRkIrVK_E"
	url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
	headers = {'content-type': 'application/json'}
	global prices
	prices=[]
	stops=[]
	carriers=[]
	carriers_2=[]
	arrivaltimes = []
	departuretimes = []
	durations = []
	second_arrivaltimes=[]
	second_departuretimes = []
	second_durations = []
	second_carriers = []
	layovers = []

	for i in range(len(result_dep)):
		params = {
			"request": {
					"slice": [
						{
						"origin": result_air[i],
						"destination": result_air[i+1],
						"date": result_dep[i],
						"maxStops": 1,
						# "maxConnectionDuration": 5000,
					}
				],
				"passengers": {
					"adultCount": adult_num,
					"childCount": kid_num,
				},
				"solutions": 30,
				# "refundable": False,
				"saleCountry": "US",
			}
		}
		response = requests.post(url, data=json.dumps(params), headers=headers)
		data = response.json()

		price = [0]*3
		stop = [0]*3
		Carrier = [0]*3
		Carriersss = [0]*3
		arrivaltime = [0]*3
		departuretime = [0]*3
		duration = [0]*3
		second_arrivaltime=[0]*3
		second_departuretime = [0]*3
		second_duration = [0]*3
		layover = [0]*3
		durationhour = [0]*3
		durationminute = [0]*3
		second_durationhour = [0]*3
		second_durationminute = [0]*3
		stophour = [0]*3
		stopminute = [0]*3
		second_carrier = [0]*3
		for j in range(3):
			price[j] = data["trips"]["tripOption"][j]["saleTotal"]
			stop[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0].get("connectionDuration", 20000)
			if stop[j] != 20000:	
				second_arrivaltime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["arrivalTime"]
				second_departuretime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["departureTime"]
				second_duration[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["duration"]
				second_carrier[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["flight"]["carrier"]+data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["flight"]["number"]
				layover[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["destination"]
		
			else:
				second_arrivaltime[j] = 0
				second_departuretime[j] = 0
				second_duration[j] = 0
				second_carrier[j] = 0
				layover[j] = 0

			Carrier[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["flight"]["carrier"]+data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["flight"]["number"]
			Carriersss[j]= data["trips"]["data"]["carrier"][j]["name"]
			arrivaltime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["arrivalTime"]
			if int(arrivaltime[j][11:13])< 12 :
			    t=arrivaltime[j][11:13]+':' +arrivaltime[j][14:16]+' AM'

			elif int(arrivaltime[j][11:13])== 13 :
			    t=arrivaltime[j][11:13]+':' +arrivaltime[j][14:16]+' PM'     

			else :
				t='0'+str(int(arrivaltime[j][11:13])-12)+':' +arrivaltime[j][14:16]+' PM'
			arrivaltime[j]= arrivaltime[j][:4]+'년'+' '+arrivaltime[j][5:7]+'월'+' '+arrivaltime[j][8:10]+'일'+' '+t

			departuretime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["departureTime"]
			if int(departuretime[j][11:13])< 12 :
			    print(departuretime[j][11:13])
			    t=departuretime[j][11:13]+':' +departuretime[j][14:16]+' AM'

			elif int(departuretime[j][11:13])== 13 :
			    print(departuretime[j][11:13])
			    t=departuretime[j][11:13]+':' +departuretime[j][14:16]+' PM'

			else :
				t='0'+str(int(departuretime[j][11:13])-12)+':' +departuretime[j][14:16]+' PM'
			departuretime[j]= departuretime[j][:4]+'년'+' '+departuretime[j][5:7]+'월'+' '+departuretime[j][8:10]+'일'+' '+t

			if stop[j] != 20000:
				if int(second_arrivaltime[j][11:13])< 12 :
				    t=second_arrivaltime[j][11:13]+':' +second_arrivaltime[j][14:16]+' AM'

				elif int(second_arrivaltime[j][11:13])== 13 :
				    t=second_arrivaltime[j][11:13]+':' +second_arrivaltime[j][14:16]+' PM'      

				else :
					t='0'+str(int(second_arrivaltime[j][11:13])-12)+':' +second_arrivaltime[j][14:16]+' PM'
				second_arrivaltime[j] = second_arrivaltime[j][:4]+'년'+' '+second_arrivaltime[j][5:7]+'월'+' '+second_arrivaltime[j][8:10]+'일'+' '+t

				if int(second_departuretime[j][11:13])< 12 :
				    print(second_departuretime[j][11:13])
				    t=second_departuretime[j][11:13]+':' +second_departuretime[j][14:16]+' AM'

				elif int(second_departuretime[j][11:13])== 13 :
				    print(second_departuretime[j][11:13])
				    t=second_departuretime[j][11:13]+':' +second_departuretime[j][14:16]+' PM'

				else :
					t='0'+str(int(second_departuretime[j][11:13])-12)+':' +second_departuretime[j][14:16]+' PM'
				second_departuretime[j]= second_departuretime[j][:4]+'년'+' '+second_departuretime[j][5:7]+'월'+' '+second_departuretime[j][8:10]+'일'+' '+t
				
			

			duration[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]

			durationhour[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]//60
			durationminute[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]%60
			if durationhour[j] < 10:
				durationhour[j]=str(0)+str(durationhour[j])
			if durationminute[j] < 10:
				durationminute[j] = str(0) + str(durationminute[j])
			duration[j] = str(durationhour[j])+"시간 "+str(durationminute[j])+"분 "

			second_durationhour[j] = second_duration[j]//60
			second_durationminute[j] = second_duration[j]%60
			if second_durationhour[j] < 10:
				durationhour[j]=str(0)+str(second_durationhour[j])
			if second_durationminute[j] < 10:
				second_durationminute[j] = str(0) + str(second_durationminute[j])
			second_duration[j] = str(second_durationhour[j])+"시간 "+str(second_durationminute[j])+"분 "

			if stop[j] != 20000:
				stophour[j] = stop[j]//60
				stopminute[j] =stop[j]%60
				if stophour[j] < 10:
					stophour[j]=str(0)+str(stophour[j])
				if stopminute[j] < 10:
					stopminute[j] = str(0) + str(stopminute[j])
				stop[j] = " "+str(stophour[j])+"시간 "+str(stopminute[j])+"분 "

				print(stop)

			prices.append(str(price[j]))
			stops.append(stop[j])
			carriers.append(Carrier[j])
			carriers_2.append(Carriersss[j])
			arrivaltimes.append(arrivaltime[j])
			departuretimes.append(departuretime[j])
			durations.append(duration[j])
			second_arrivaltimes.append(second_arrivaltime[j])
			second_departuretimes.append(second_departuretime[j])
			second_durations.append(second_duration[j])
			second_carriers.append(second_carrier[j])
			layovers.append(layover[j])

	real_price =[]	
	real_stop =[]
	real_carrier =[]
	real_carrier2 =[]
	real_arrivaltime = []
	real_departuretime = []
	real_duration = []
	real_radio=[]
	real_second_arrivaltime = []
	real_second_departuretime= []
	real_second_duration = []
	real_second_carrier = []
	real_layover = []
	for i in range(24):
		real_price.append(str("price")+str(i))
		real_stop.append(str("stop")+str(i))
		real_carrier.append(str("carrier")+str(i))
		real_carrier2.append(str("carrier2_")+str(i))
		real_arrivaltime.append(str("arrivaltime")+str(i))
		real_departuretime.append(str("departuretime")+str(i))
		real_duration.append(str("duration")+str(i))
		real_second_arrivaltime.append(str("second_arrivaltime")+str(i))
		real_second_departuretime.append(str("second_departuretime")+str(i))
		real_second_duration.append(str("second_duration")+str(i))
		real_second_carrier.append(str("second_carrier")+str(i))
		real_layover.append(str("layover")+str(i))

	for i in range(32):	
		real_radio.append(str("radio")+str(i))	



    
	for i in range(len(real_price)-len(prices)):
		prices.append(0)
		stops.append(0)
		carriers.append(0)
		carriers_2.append(0)
		arrivaltimes.append(0)
		departuretimes.append(0)
		durations.append(0)
		second_arrivaltimes.append(0)
		second_departuretimes.append(0)
		second_durations.append(0)
		second_carriers.append(0)
		layovers.append(0)

	radios=[]    
	for i in range(8):
		radios.append(str("radio")+str(i))
	radios=radios*4
	radios.sort()

	for i in zip(real_radio,radios):	
		globals()[i[0]]=i[1]


	for i in zip(real_price,prices,real_stop,stops,real_carrier,carriers,real_carrier2,carriers_2,real_arrivaltime,arrivaltimes,real_departuretime,departuretimes,real_duration,durations,real_second_arrivaltime,second_arrivaltimes,real_second_departuretime,second_departuretimes,real_second_duration,second_durations,real_second_carrier,second_carriers,real_layover,layovers):
		if i[1] != 0:
			globals()[i[0]]=float(i[1][3:])
			globals()[i[2]]=i[3]
			globals()[i[4]]=i[5]
			globals()[i[6]]=i[7]
			globals()[i[8]]=i[9]
			globals()[i[10]]=i[11]
			globals()[i[12]]=i[13]
			globals()[i[14]]=i[15]
			globals()[i[16]]=i[17]
			globals()[i[18]]=i[19]
			globals()[i[20]]=i[21]
			globals()[i[22]]=i[23]
		else:
			globals()[i[0]]=i[1]
			globals()[i[2]]=i[3]
			globals()[i[4]]=i[5]
			globals()[i[6]]=i[7]
			globals()[i[8]]=i[9]
			globals()[i[10]]=i[11]
			globals()[i[12]]=i[13]
			globals()[i[14]]=i[15]
			globals()[i[16]]=i[17]
			globals()[i[18]]=i[19]
			globals()[i[20]]=i[21]
			globals()[i[22]]=i[23]

	conn = sqlite3.connect("lapistadb.db")
	eurail_cost = []
	eurail_dep = []
	eurail_arr = []
	eurail_time = []
	e_dep_date = []
	for i in range(len(result_air) - 1):
		cursor3 = conn.execute(
			"SELECT PRICE,DEP_TIME,ARR_TIME,REQUIRED_TIME from eurail where dep_date=(?) and r_origin=(?) and r_dest=(?)",
			(result_dep[i], result_air[i], result_air[i + 1]))
		eurail_cost.append([])
		eurail_dep.append([])
		eurail_arr.append([])
		eurail_time.append([])
		e_dep_date.append(result_dep[i])
		for row in cursor3:
			eurail_cost[i].append(row[0])
			eurail_dep[i].append(row[1])
			eurail_arr[i].append(row[2])
			eurail_time[i].append(row[3])
		else:
			eurail_cost[i].append(0)
			eurail_dep[i].append(0)
			eurail_arr[i].append(0)
			eurail_time[i].append(0)

	while len(e_dep_date) != 8:
		e_dep_date.append(0)		

	eurail_top_c = [0] * 8
	for i in range(len(eurail_cost)):
		for j in range(len(eurail_cost[i])):
			eurail_top_c[i] = eurail_cost[i][0]

	eurail_top_d = [0] * 8
	for i in range(len(eurail_dep)):
		for j in range(len(eurail_dep[i])):
			eurail_top_d[i] = eurail_dep[i][0]

	eurail_top_a = [0] * 8
	for i in range(len(eurail_arr)):
		for j in range(len(eurail_arr[i])):
			eurail_top_a[i] = eurail_arr[i][0]

	eurail_top_t = [0] * 8
	for i in range(len(eurail_time)):
		for j in range(len(eurail_time[i])):
			eurail_top_t[i] = eurail_time[i][0]

	eurail_info = ['---------------유레일스케쥴--------------'] * 8
	for i in range(len(eurail_cost)):
		for j in range(len(eurail_cost[i])):
			if eurail_cost[i][j] != 0:
				a = '-------$' + str(eurail_cost[i][j]) + ' ' + str(eurail_dep[i][j]) + ' ' + str(eurail_time[i][j]) + '--------'
				eurail_info[i] = ''.join((eurail_info[i], a))
	print(eurail_info)

	Eurail = 'Eurail'
	price_t1=[22,34,55]
	price_t2=0
	E_di = 30000
	prices1=[price0,price1,price2,eurail_top_c[0]]
	prices2=[price3,price4,price5,eurail_top_c[1]]
	prices3=[price6,price7,price8,eurail_top_c[2]]
	prices4=[price9,price10,price11,eurail_top_c[3]]
	prices5=[price12,price13,price14,eurail_top_c[4]]
	prices6=[price15,price16,price17,eurail_top_c[5]]
	prices7=[price18,price19,price20,eurail_top_c[6]]
	prices8=[price21,price22,price23,eurail_top_c[7]]
	global price_all
	price_all=[]
	price_all=[prices1,prices2,prices3,prices4,prices5,prices6,prices7,prices8]
	stops1=[stop0,stop1,stop2,E_di]
	stops2=[stop3,stop4,stop5,E_di]
	stops3=[stop6,stop7,stop8,E_di]
	stops4=[stop9,stop10,stop11,E_di]
	stops5=[stop12,stop13,stop14,E_di]
	stops6=[stop15,stop16,stop17,E_di]
	stops7=[stop18,stop19,stop20,E_di]
	stops8=[stop21,stop22,stop23,E_di]
	carriers1=[carrier0,carrier1,carrier2,Eurail]
	carriers2=[carrier3,carrier4,carrier5,Eurail]
	carriers3=[carrier6,carrier7,carrier8,Eurail]
	carriers4=[carrier9,carrier10,carrier11,Eurail]
	carriers5=[carrier12,carrier13,carrier14,Eurail]
	carriers6=[carrier15,carrier16,carrier17,Eurail]
	carriers7=[carrier18,carrier19,carrier20,Eurail]
	carriers8=[carrier21,carrier22,carrier23,Eurail]
	carriers2_1=[carrier2_0,carrier2_1,carrier2_2,Eurail]
	carriers2_2=[carrier2_3,carrier2_4,carrier2_5,Eurail]
	carriers2_3=[carrier2_6,carrier2_7,carrier2_8,Eurail]
	carriers2_4=[carrier2_9,carrier2_10,carrier2_11,Eurail]
	carriers2_5=[carrier2_12,carrier2_13,carrier2_14,Eurail]
	carriers2_6=[carrier2_15,carrier2_16,carrier2_17,Eurail]
	carriers2_7=[carrier2_18,carrier2_19,carrier2_20,Eurail]
	carriers2_8=[carrier2_21,carrier2_22,carrier2_23,Eurail]
	arrivaltimes1=[arrivaltime0,arrivaltime1,arrivaltime2,eurail_top_a[0]]
	arrivaltimes2=[arrivaltime3,arrivaltime4,arrivaltime5,eurail_top_a[1]]
	arrivaltimes3=[arrivaltime6,arrivaltime7,arrivaltime8,eurail_top_a[2]]
	arrivaltimes4=[arrivaltime9,arrivaltime10,arrivaltime11,eurail_top_a[3]]
	arrivaltimes5=[arrivaltime12,arrivaltime13,arrivaltime14,eurail_top_a[4]]
	arrivaltimes6=[arrivaltime15,arrivaltime16,arrivaltime17,eurail_top_a[5]]
	arrivaltimes7=[arrivaltime18,arrivaltime19,arrivaltime20,eurail_top_a[6]]
	arrivaltimes8=[arrivaltime21,arrivaltime22,arrivaltime23,eurail_top_a[7]]
	departuretimes1=[departuretime0,departuretime1,departuretime2,e_dep_date[0]]
	departuretimes2=[departuretime3,departuretime4,departuretime5,e_dep_date[1]]
	departuretimes3=[departuretime6,departuretime7,departuretime8,e_dep_date[2]]
	departuretimes4=[departuretime9,departuretime10,departuretime11,e_dep_date[3]]
	departuretimes5=[departuretime12,departuretime13,departuretime14,e_dep_date[4]]
	departuretimes6=[departuretime15,departuretime16,departuretime17,e_dep_date[5]]
	departuretimes7=[departuretime18,departuretime19,departuretime20,e_dep_date[6]]
	departuretimes8=[departuretime21,departuretime22,departuretime23,e_dep_date[7]]
	durations1=[duration0,duration1,duration2,eurail_top_t[0]]
	durations2=[duration3,duration4,duration5,eurail_top_t[1]]
	durations3=[duration6,duration7,duration8,eurail_top_t[2]]
	durations4=[duration9,duration10,duration11,eurail_top_t[3]]
	durations5=[duration12,duration13,duration14,eurail_top_t[4]]
	durations6=[duration15,duration16,duration17,eurail_top_t[5]]
	durations7=[duration18,duration19,duration20,eurail_top_t[6]]
	durations8=[duration21,duration22,duration23,eurail_top_t[7]]
	radios1=[radio0,radio1,radio2,radio3]
	radios2=[radio4,radio5,radio6,radio7]
	radios3=[radio8,radio9,radio10,radio11]
	radios4=[radio12,radio13,radio14,radio15]
	radios5=[radio16,radio17,radio18,radio19]
	radios6=[radio20,radio21,radio22,radio23]
	radios7=[radio24,radio25,radio26,radio27]
	radios8=[radio28,radio29,radio30,radio31]
	second_arrivaltimes1=[second_arrivaltime0,second_arrivaltime1,second_arrivaltime2,price_t1]
	second_arrivaltimes2=[second_arrivaltime3,second_arrivaltime4,second_arrivaltime5,price_t1]
	second_arrivaltimes3=[second_arrivaltime6,second_arrivaltime7,second_arrivaltime8,price_t1]
	second_arrivaltimes4=[second_arrivaltime9,second_arrivaltime10,second_arrivaltime11,price_t2]
	second_arrivaltimes5=[second_arrivaltime12,second_arrivaltime13,second_arrivaltime14,price_t2]
	second_arrivaltimes6=[second_arrivaltime15,second_arrivaltime16,second_arrivaltime17,price_t2]
	second_arrivaltimes7=[second_arrivaltime18,second_arrivaltime19,second_arrivaltime20,price_t2]
	second_arrivaltimes8=[second_arrivaltime21,second_arrivaltime22,second_arrivaltime23,price_t2]
	second_departuretimes1=[second_departuretime0,second_departuretime1,second_departuretime2,price_t1]
	second_departuretimes2=[second_departuretime3,second_departuretime4,second_departuretime5,price_t1]
	second_departuretimes3=[second_departuretime6,second_departuretime7,second_departuretime8,price_t1]
	second_departuretimes4=[second_departuretime9,second_departuretime10,second_departuretime11,price_t2]
	second_departuretimes5=[second_departuretime12,second_departuretime13,second_departuretime14,price_t2]
	second_departuretimes6=[second_departuretime15,second_departuretime16,second_departuretime17,price_t2]
	second_departuretimes7=[second_departuretime18,second_departuretime19,second_departuretime20,price_t2]
	second_departuretimes8=[second_departuretime21,second_departuretime22,second_departuretime23,price_t2]
	second_durations1=[second_duration0,second_duration1,second_duration2,price_t1]
	second_durations2=[second_duration3,second_duration4,second_duration5,price_t1]
	second_durations3=[second_duration6,second_duration7,second_duration8,price_t1]
	second_durations4=[second_duration9,second_duration10,second_duration11,price_t2]
	second_durations5=[second_duration12,second_duration13,second_duration14,price_t2]
	second_durations6=[second_duration15,second_duration16,second_duration17,price_t2]
	second_durations7=[second_duration18,second_duration19,second_duration20,price_t2]
	second_durations8=[second_duration21,second_duration22,second_duration23,price_t2]
	second_carriers1=[second_carrier0,second_carrier1,second_carrier2,price_t1]
	second_carriers2=[second_carrier3,second_carrier4,second_carrier5,price_t1]
	second_carriers3=[second_carrier6,second_carrier7,second_carrier8,price_t1]
	second_carriers4=[second_carrier9,second_carrier10,second_carrier11,price_t1]
	second_carriers5=[second_carrier12,second_carrier13,second_carrier14,price_t1]
	second_carriers6=[second_carrier15,second_carrier16,second_carrier17,price_t1]
	second_carriers7=[second_carrier18,second_carrier19,second_carrier20,price_t1]
	second_carriers8=[second_carrier21,second_carrier22,second_carrier23,price_t1]
	layovers1=[layover0,layover1,layover2,eurail_info[0]]
	layovers2=[layover3,layover4,layover5,eurail_info[1]]
	layovers3=[layover6,layover7,layover8,eurail_info[2]]
	layovers4=[layover9,layover10,layover11,eurail_info[3]]
	layovers5=[layover12,layover13,layover14,eurail_info[4]]
	layovers6=[layover15,layover16,layover17,eurail_info[5]]
	layovers7=[layover18,layover19,layover20,eurail_info[6]]
	layovers8=[layover21,layover22,layover23,eurail_info[7]]

	result_st2=result_st[1:]
	global kkk
	kkk=[]
	kkk=[zip(prices1,stops1,carriers1,carriers2_1,arrivaltimes1,departuretimes1,durations1,radios1,second_departuretimes1,second_arrivaltimes1,second_durations1,second_carriers1,layovers1),zip(prices2,stops2,carriers2,carriers2_2,arrivaltimes2,departuretimes2,durations2,radios2,second_departuretimes2,second_arrivaltimes2,second_durations2,second_carriers2,layovers2),zip(prices3,stops3,carriers3,carriers2_3,arrivaltimes3,departuretimes3,durations3,radios3,second_departuretimes3,second_arrivaltimes3,second_durations3,second_carriers3,layovers3),zip(prices4,stops4,carriers4,carriers2_4,arrivaltimes4,departuretimes4,durations4,radios4,second_departuretimes4,second_arrivaltimes4,second_durations4,second_carriers4,layovers4),zip(prices5,stops5,carriers5,carriers2_5,arrivaltimes5,departuretimes5,durations5,radios5,second_departuretimes5,second_arrivaltimes5,second_durations5,second_carriers5,layovers5),zip(prices6,stops6,carriers6,carriers2_6,arrivaltimes6,departuretimes6,durations6,radios6,second_departuretimes6,second_arrivaltimes6,second_durations6,second_carriers6,layovers6),zip(prices7,stops7,carriers7,carriers2_7,arrivaltimes7,departuretimes7,durations7,radios7,second_departuretimes7,second_arrivaltimes7,second_durations7,second_carriers7,layovers7),zip(prices8,stops8,carriers8,carriers2_8,arrivaltimes8,departuretimes8,durations8,radios8,second_departuretimes8,second_arrivaltimes8,second_durations8,second_carriers8,layovers8)]

	global location_real
	location_real=[]
	for i in result_air3:
	   a=airport_all.index(i)
	   location_real.append(location_all[a-1])

	global first_dep
	first_dep=[]
  	c=airport_all.index(result_air3[0])
	first_dep=location_all[c-1]

	global air_result_kor   
	air_result_kor = []
   	for i in result_air3:
		air_kor_name = models.Airport.objects.get(air_name = i)
		air_result_kor.append(air_kor_name.city_name)

	global results2, results3
	results2=[]
	results3=[]	
	results2=zip(air_result_kor,result_st2)
	results3=zip(air_result_kor,result_st2,result_air3)

	return render(request, 'pages/price.html', {"adult_num": adult_num,
												 "kid_num": kid_num,
												 "depday": depday,
												 "arrday": arrday,
												 "location_real":location_real,
												 "result_air":result_air,
											     "kkk": kkk,
											     "real_air":real_air,
											     "results2":results2,
											     "result_air3":result_air3,
											     "air_result_kor" : air_result_kor,
											     "results3":results3,
											     "lastcity":lastcity,
											     "first_dep":first_dep,
											     })
def apiresult(request):
	return render(request, 'pages/result.html',{"adult_num": adult_num,
												 "kid_num": kid_num,
												 "depday": depday,
												 "arrday": arrday,
												 "location_real":location_real,
												 "result_air":result_air,
											     "kkk": kkk,
											     "real_air":real_air,
											     "results2":results2,
											     "result_air3":result_air3,
											     "air_result_kor" : air_result_kor,
											     "results3":results3,
											     "lastcity":lastcity,
											     "first_dep": first_dep
											     })

def research(request):
	lastcity = request.POST.get("lastcity")
	st=request.POST.get("st")
	pc=request.POST.get("pc")
	
	alpha = int(pc)
	beta = int(st)

	staytime = [0]
	air=['ICN']
	for i in result_air3:
		staytime.append(int(str(request.POST.get(i))))
		air.append(i)

   	global ST
	ST=staytime

   	global lastcity
	if lastcity != '100':
		lastcity = air.index(lastcity)
	else:
		lastcity=100

	result_air=[]
	result_dep=[]
	result_st=[]
	global order_fix
	order_fix=request.POST.get("order_fix")
	print(order_fix)

	if order_fix != None:
		print('YES')
		air_dest = air[1:]
		air_dest.append('ICN')
		order(air,depday,arrday,result_st,result_air,result_dep,alpha,beta,ST,alpha,beta)
	else:
		deftsp(air,depday,arrday,result_st,result_air,result_dep,alpha,beta,ST,lastcity,special_date)
	
	if len(result_st) < 1:
		return render(request, 'pages/mainerror.html')

	global result_air1,result_air2,result_air3
	result_air1=[]
	result_air2=[]
	result_air3=[]
	print("new",result_air)
	result_air1=result_air[:(len(result_air)-1)]
	result_air2=result_air[1:]
	result_air3=result_air[1:(len(result_air)-1)]
	list_num=len(result_air3)
	real_air = []
	real_air = zip(result_air1,result_air2,result_dep)

	global real_air

	response = [0]*(len(result_dep))
	api_key= [0]*(len(result_dep))
	url=[0]*(len(result_dep))
	headers=[0]*(len(result_dep))
	params=[0]*(len(result_dep))

	# api_key="AIzaSyDbpKpdqdIlItEhipc0j6fATk4iHaWdzUw"
	api_key = "AIzaSyDiYhxOy8UR29FtgCQHsZz_7yxRkIrVK_E"
	url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
	headers = {'content-type': 'application/json'}
	global prices
	prices=[]
	stops=[]
	carriers=[]
	carriers_2=[]
	arrivaltimes = []
	departuretimes = []
	durations = []
	second_arrivaltimes=[]
	second_departuretimes = []
	second_durations = []
	second_carriers = []
	layovers = []

	for i in range(len(result_dep)):
		params = {
			"request": {
					"slice": [
						{
						"origin": result_air[i],
						"destination": result_air[i+1],
						"date": result_dep[i],
						"maxStops": 1,
						# "maxConnectionDuration": 5000,
					}
				],
				"passengers": {
					"adultCount": adult_num,
					"childCount": kid_num,
				},
				"solutions": 30,
				# "refundable": False,
				"saleCountry": "US",
			}
		}
		response = requests.post(url, data=json.dumps(params), headers=headers)
		data = response.json()

		price = [0]*3
		stop = [0]*3
		Carrier = [0]*3
		Carriersss = [0]*3
		arrivaltime = [0]*3
		departuretime = [0]*3
		duration = [0]*3
		second_arrivaltime=[0]*3
		second_departuretime = [0]*3
		second_duration = [0]*3
		layover = [0]*3
		durationhour = [0]*3
		durationminute = [0]*3
		second_durationhour = [0]*3
		second_durationminute = [0]*3
		stophour = [0]*3
		stopminute = [0]*3
		second_carrier = [0]*3
		for j in range(3):
			price[j] = data["trips"]["tripOption"][j]["saleTotal"]
			stop[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0].get("connectionDuration", 20000)
			if stop[j] != 20000:	
				second_arrivaltime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["arrivalTime"]
				second_departuretime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["departureTime"]
				second_duration[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["duration"]
				second_carrier[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["flight"]["carrier"]+data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["flight"]["number"]
				layover[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["destination"]
		
			else:
				second_arrivaltime[j] = 0
				second_departuretime[j] = 0
				second_duration[j] = 0
				second_carrier[j] = 0
				layover[j] = 0

			Carrier[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["flight"]["carrier"]+data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["flight"]["number"]
			Carriersss[j]= data["trips"]["data"]["carrier"][j]["name"]
			arrivaltime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["arrivalTime"]
			if int(arrivaltime[j][11:13])< 12 :
			    t=arrivaltime[j][11:13]+':' +arrivaltime[j][14:16]+' AM'

			elif int(arrivaltime[j][11:13])== 13 :
			    t=arrivaltime[j][11:13]+':' +arrivaltime[j][14:16]+' PM'     

			else :
				t='0'+str(int(arrivaltime[j][11:13])-12)+':' +arrivaltime[j][14:16]+' PM'
			arrivaltime[j]= arrivaltime[j][:4]+'년'+' '+arrivaltime[j][5:7]+'월'+' '+arrivaltime[j][8:10]+'일'+' '+t

			departuretime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["departureTime"]
			if int(departuretime[j][11:13])< 12 :
			    print(departuretime[j][11:13])
			    t=departuretime[j][11:13]+':' +departuretime[j][14:16]+' AM'

			elif int(departuretime[j][11:13])== 13 :
			    print(departuretime[j][11:13])
			    t=departuretime[j][11:13]+':' +departuretime[j][14:16]+' PM'

			else :
				t='0'+str(int(departuretime[j][11:13])-12)+':' +departuretime[j][14:16]+' PM'
			departuretime[j]= departuretime[j][:4]+'년'+' '+departuretime[j][5:7]+'월'+' '+departuretime[j][8:10]+'일'+' '+t

			if stop[j] != 20000:
				if int(second_arrivaltime[j][11:13])< 12 :
				    t=second_arrivaltime[j][11:13]+':' +second_arrivaltime[j][14:16]+' AM'

				elif int(second_arrivaltime[j][11:13])== 13 :
				    t=second_arrivaltime[j][11:13]+':' +second_arrivaltime[j][14:16]+' PM'      

				else :
					t='0'+str(int(second_arrivaltime[j][11:13])-12)+':' +second_arrivaltime[j][14:16]+' PM'
				second_arrivaltime[j] = second_arrivaltime[j][:4]+'년'+' '+second_arrivaltime[j][5:7]+'월'+' '+second_arrivaltime[j][8:10]+'일'+' '+t

				if int(second_departuretime[j][11:13])< 12 :
				    print(second_departuretime[j][11:13])
				    t=second_departuretime[j][11:13]+':' +second_departuretime[j][14:16]+' AM'

				elif int(second_departuretime[j][11:13])== 13 :
				    print(second_departuretime[j][11:13])
				    t=second_departuretime[j][11:13]+':' +second_departuretime[j][14:16]+' PM' 

				else :
					t='0'+str(int(second_departuretime[j][11:13])-12)+':' +second_departuretime[j][14:16]+' PM'
				second_departuretime[j]= second_departuretime[j][:4]+'년'+' '+second_departuretime[j][5:7]+'월'+' '+second_departuretime[j][8:10]+'일'+' '+t
				
			

			duration[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]

			durationhour[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]//60
			durationminute[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]%60
			if durationhour[j] < 10:
				durationhour[j]=str(0)+str(durationhour[j])
			if durationminute[j] < 10:
				durationminute[j] = str(0) + str(durationminute[j])
			duration[j] = str(durationhour[j])+"시간 "+str(durationminute[j])+"분 "

			second_durationhour[j] = second_duration[j]//60
			second_durationminute[j] = second_duration[j]%60
			if second_durationhour[j] < 10:
				durationhour[j]=str(0)+str(second_durationhour[j])
			if second_durationminute[j] < 10:
				second_durationminute[j] = str(0) + str(second_durationminute[j])
			second_duration[j] = str(second_durationhour[j])+"시간 "+str(second_durationminute[j])+"분 "

			if stop[j] != 20000:
				stophour[j] = stop[j]//60
				stopminute[j] =stop[j]%60
				if stophour[j] < 10:
					stophour[j]=str(0)+str(stophour[j])
				if stopminute[j] < 10:
					stopminute[j] = str(0) + str(stopminute[j])
				stop[j] = " "+str(stophour[j])+"시간 "+str(stopminute[j])+"분 "

				print(stop)

			prices.append(str(price[j]))
			stops.append(stop[j])
			carriers.append(Carrier[j])
			carriers_2.append(Carriersss[j])
			arrivaltimes.append(arrivaltime[j])
			departuretimes.append(departuretime[j])
			durations.append(duration[j])
			second_arrivaltimes.append(second_arrivaltime[j])
			second_departuretimes.append(second_departuretime[j])
			second_durations.append(second_duration[j])
			second_carriers.append(second_carrier[j])
			layovers.append(layover[j])

	real_price =[]	
	real_stop =[]
	real_carrier =[]
	real_carrier2 =[]
	real_arrivaltime = []
	real_departuretime = []
	real_duration = []
	real_radio=[]
	real_second_arrivaltime = []
	real_second_departuretime= []
	real_second_duration = []
	real_second_carrier = []
	real_layover = []
	for i in range(24):
		real_price.append(str("price")+str(i))
		real_stop.append(str("stop")+str(i))
		real_carrier.append(str("carrier")+str(i))
		real_carrier2.append(str("carrier2_")+str(i))
		real_arrivaltime.append(str("arrivaltime")+str(i))
		real_departuretime.append(str("departuretime")+str(i))
		real_duration.append(str("duration")+str(i))
		real_second_arrivaltime.append(str("second_arrivaltime")+str(i))
		real_second_departuretime.append(str("second_departuretime")+str(i))
		real_second_duration.append(str("second_duration")+str(i))
		real_second_carrier.append(str("second_carrier")+str(i))
		real_layover.append(str("layover")+str(i))

	for i in range(32):	
		real_radio.append(str("radio")+str(i))	

	for i in range(len(real_price)-len(prices)):
		prices.append(0)
		stops.append(0)
		carriers.append(0)
		carriers_2.append(0)
		arrivaltimes.append(0)
		departuretimes.append(0)
		durations.append(0)
		second_arrivaltimes.append(0)
		second_departuretimes.append(0)
		second_durations.append(0)
		second_carriers.append(0)
		layovers.append(0)

	radios=[]    
	for i in range(8):
		radios.append(str("radio")+str(i))
	radios=radios*4
	radios.sort()

	for i in zip(real_radio,radios):	
		globals()[i[0]]=i[1]


	for i in zip(real_price,prices,real_stop,stops,real_carrier,carriers,real_carrier2,carriers_2,real_arrivaltime,arrivaltimes,real_departuretime,departuretimes,real_duration,durations,real_second_arrivaltime,second_arrivaltimes,real_second_departuretime,second_departuretimes,real_second_duration,second_durations,real_second_carrier,second_carriers,real_layover,layovers):
		if i[1] != 0:
			globals()[i[0]]=float(i[1][3:])
			globals()[i[2]]=i[3]
			globals()[i[4]]=i[5]
			globals()[i[6]]=i[7]
			globals()[i[8]]=i[9]
			globals()[i[10]]=i[11]
			globals()[i[12]]=i[13]
			globals()[i[14]]=i[15]
			globals()[i[16]]=i[17]
			globals()[i[18]]=i[19]
			globals()[i[20]]=i[21]
			globals()[i[22]]=i[23]
		else:
			globals()[i[0]]=i[1]
			globals()[i[2]]=i[3]
			globals()[i[4]]=i[5]
			globals()[i[6]]=i[7]
			globals()[i[8]]=i[9]
			globals()[i[10]]=i[11]
			globals()[i[12]]=i[13]
			globals()[i[14]]=i[15]
			globals()[i[16]]=i[17]
			globals()[i[18]]=i[19]
			globals()[i[20]]=i[21]
			globals()[i[22]]=i[23]

	conn = sqlite3.connect("lapistadb.db")
	eurail_cost = []
	eurail_dep = []
	eurail_arr = []
	eurail_time = []
	e_dep_date = []
	for i in range(len(result_air) - 1):
		cursor3 = conn.execute(
			"SELECT PRICE,DEP_TIME,ARR_TIME,REQUIRED_TIME from eurail where dep_date=(?) and r_origin=(?) and r_dest=(?)",
			(result_dep[i], result_air[i], result_air[i + 1]))
		eurail_cost.append([])
		eurail_dep.append([])
		eurail_arr.append([])
		eurail_time.append([])
		e_dep_date.append(result_dep[i])
		for row in cursor3:
			eurail_cost[i].append(row[0])
			eurail_dep[i].append(row[1])
			eurail_arr[i].append(row[2])
			eurail_time[i].append(row[3])
		else:
			eurail_cost[i].append(0)
			eurail_dep[i].append(0)
			eurail_arr[i].append(0)
			eurail_time[i].append(0)

	while len(e_dep_date) != 8:
		e_dep_date.append(0)		

	eurail_top_c = [0] * 8
	for i in range(len(eurail_cost)):
		for j in range(len(eurail_cost[i])):
			eurail_top_c[i] = eurail_cost[i][0]

	eurail_top_d = [0] * 8
	for i in range(len(eurail_dep)):
		for j in range(len(eurail_dep[i])):
			eurail_top_d[i] = eurail_dep[i][0]

	eurail_top_a = [0] * 8
	for i in range(len(eurail_arr)):
		for j in range(len(eurail_arr[i])):
			eurail_top_a[i] = eurail_arr[i][0]

	eurail_top_t = [0] * 8
	for i in range(len(eurail_time)):
		for j in range(len(eurail_time[i])):
			eurail_top_t[i] = eurail_time[i][0]

	eurail_info = ['---------------유레일스케쥴--------------'] * 8
	for i in range(len(eurail_cost)):
		for j in range(len(eurail_cost[i])):
			if eurail_cost[i][j] != 0:
				a = '-------$' + str(eurail_cost[i][j]) + ' ' + str(eurail_dep[i][j]) + ' ' + str(eurail_time[i][j]) + '--------'
				eurail_info[i] = ''.join((eurail_info[i], a))
	print(eurail_info)

	Eurail = 'Eurail'
	price_t1=[22,34,55]
	price_t2=0
	E_di = 30000
	prices1=[price0,price1,price2,eurail_top_c[0]]
	prices2=[price3,price4,price5,eurail_top_c[1]]
	prices3=[price6,price7,price8,eurail_top_c[2]]
	prices4=[price9,price10,price11,eurail_top_c[3]]
	prices5=[price12,price13,price14,eurail_top_c[4]]
	prices6=[price15,price16,price17,eurail_top_c[5]]
	prices7=[price18,price19,price20,eurail_top_c[6]]
	prices8=[price21,price22,price23,eurail_top_c[7]]
	global price_all
	price_all=[]
	price_all=[prices1,prices2,prices3,prices4,prices5,prices6,prices7,prices8]
	stops1=[stop0,stop1,stop2,E_di]
	stops2=[stop3,stop4,stop5,E_di]
	stops3=[stop6,stop7,stop8,E_di]
	stops4=[stop9,stop10,stop11,E_di]
	stops5=[stop12,stop13,stop14,E_di]
	stops6=[stop15,stop16,stop17,E_di]
	stops7=[stop18,stop19,stop20,E_di]
	stops8=[stop21,stop22,stop23,E_di]
	carriers1=[carrier0,carrier1,carrier2,Eurail]
	carriers2=[carrier3,carrier4,carrier5,Eurail]
	carriers3=[carrier6,carrier7,carrier8,Eurail]
	carriers4=[carrier9,carrier10,carrier11,Eurail]
	carriers5=[carrier12,carrier13,carrier14,Eurail]
	carriers6=[carrier15,carrier16,carrier17,Eurail]
	carriers7=[carrier18,carrier19,carrier20,Eurail]
	carriers8=[carrier21,carrier22,carrier23,Eurail]
	carriers2_1=[carrier2_0,carrier2_1,carrier2_2,Eurail]
	carriers2_2=[carrier2_3,carrier2_4,carrier2_5,Eurail]
	carriers2_3=[carrier2_6,carrier2_7,carrier2_8,Eurail]
	carriers2_4=[carrier2_9,carrier2_10,carrier2_11,Eurail]
	carriers2_5=[carrier2_12,carrier2_13,carrier2_14,Eurail]
	carriers2_6=[carrier2_15,carrier2_16,carrier2_17,Eurail]
	carriers2_7=[carrier2_18,carrier2_19,carrier2_20,Eurail]
	carriers2_8=[carrier2_21,carrier2_22,carrier2_23,Eurail]
	arrivaltimes1=[arrivaltime0,arrivaltime1,arrivaltime2,eurail_top_a[0]]
	arrivaltimes2=[arrivaltime3,arrivaltime4,arrivaltime5,eurail_top_a[1]]
	arrivaltimes3=[arrivaltime6,arrivaltime7,arrivaltime8,eurail_top_a[2]]
	arrivaltimes4=[arrivaltime9,arrivaltime10,arrivaltime11,eurail_top_a[3]]
	arrivaltimes5=[arrivaltime12,arrivaltime13,arrivaltime14,eurail_top_a[4]]
	arrivaltimes6=[arrivaltime15,arrivaltime16,arrivaltime17,eurail_top_a[5]]
	arrivaltimes7=[arrivaltime18,arrivaltime19,arrivaltime20,eurail_top_a[6]]
	arrivaltimes8=[arrivaltime21,arrivaltime22,arrivaltime23,eurail_top_a[7]]
	departuretimes1=[departuretime0,departuretime1,departuretime2,e_dep_date[0]]
	departuretimes2=[departuretime3,departuretime4,departuretime5,e_dep_date[1]]
	departuretimes3=[departuretime6,departuretime7,departuretime8,e_dep_date[2]]
	departuretimes4=[departuretime9,departuretime10,departuretime11,e_dep_date[3]]
	departuretimes5=[departuretime12,departuretime13,departuretime14,e_dep_date[4]]
	departuretimes6=[departuretime15,departuretime16,departuretime17,e_dep_date[5]]
	departuretimes7=[departuretime18,departuretime19,departuretime20,e_dep_date[6]]
	departuretimes8=[departuretime21,departuretime22,departuretime23,e_dep_date[7]]
	durations1=[duration0,duration1,duration2,eurail_top_t[0]]
	durations2=[duration3,duration4,duration5,eurail_top_t[1]]
	durations3=[duration6,duration7,duration8,eurail_top_t[2]]
	durations4=[duration9,duration10,duration11,eurail_top_t[3]]
	durations5=[duration12,duration13,duration14,eurail_top_t[4]]
	durations6=[duration15,duration16,duration17,eurail_top_t[5]]
	durations7=[duration18,duration19,duration20,eurail_top_t[6]]
	durations8=[duration21,duration22,duration23,eurail_top_t[7]]
	radios1=[radio0,radio1,radio2,radio3]
	radios2=[radio4,radio5,radio6,radio7]
	radios3=[radio8,radio9,radio10,radio11]
	radios4=[radio12,radio13,radio14,radio15]
	radios5=[radio16,radio17,radio18,radio19]
	radios6=[radio20,radio21,radio22,radio23]
	radios7=[radio24,radio25,radio26,radio27]
	radios8=[radio28,radio29,radio30,radio31]
	second_arrivaltimes1=[second_arrivaltime0,second_arrivaltime1,second_arrivaltime2,price_t1]
	second_arrivaltimes2=[second_arrivaltime3,second_arrivaltime4,second_arrivaltime5,price_t1]
	second_arrivaltimes3=[second_arrivaltime6,second_arrivaltime7,second_arrivaltime8,price_t1]
	second_arrivaltimes4=[second_arrivaltime9,second_arrivaltime10,second_arrivaltime11,price_t2]
	second_arrivaltimes5=[second_arrivaltime12,second_arrivaltime13,second_arrivaltime14,price_t2]
	second_arrivaltimes6=[second_arrivaltime15,second_arrivaltime16,second_arrivaltime17,price_t2]
	second_arrivaltimes7=[second_arrivaltime18,second_arrivaltime19,second_arrivaltime20,price_t2]
	second_arrivaltimes8=[second_arrivaltime21,second_arrivaltime22,second_arrivaltime23,price_t2]
	second_departuretimes1=[second_departuretime0,second_departuretime1,second_departuretime2,price_t1]
	second_departuretimes2=[second_departuretime3,second_departuretime4,second_departuretime5,price_t1]
	second_departuretimes3=[second_departuretime6,second_departuretime7,second_departuretime8,price_t1]
	second_departuretimes4=[second_departuretime9,second_departuretime10,second_departuretime11,price_t2]
	second_departuretimes5=[second_departuretime12,second_departuretime13,second_departuretime14,price_t2]
	second_departuretimes6=[second_departuretime15,second_departuretime16,second_departuretime17,price_t2]
	second_departuretimes7=[second_departuretime18,second_departuretime19,second_departuretime20,price_t2]
	second_departuretimes8=[second_departuretime21,second_departuretime22,second_departuretime23,price_t2]
	second_durations1=[second_duration0,second_duration1,second_duration2,price_t1]
	second_durations2=[second_duration3,second_duration4,second_duration5,price_t1]
	second_durations3=[second_duration6,second_duration7,second_duration8,price_t1]
	second_durations4=[second_duration9,second_duration10,second_duration11,price_t2]
	second_durations5=[second_duration12,second_duration13,second_duration14,price_t2]
	second_durations6=[second_duration15,second_duration16,second_duration17,price_t2]
	second_durations7=[second_duration18,second_duration19,second_duration20,price_t2]
	second_durations8=[second_duration21,second_duration22,second_duration23,price_t2]
	second_carriers1=[second_carrier0,second_carrier1,second_carrier2,price_t1]
	second_carriers2=[second_carrier3,second_carrier4,second_carrier5,price_t1]
	second_carriers3=[second_carrier6,second_carrier7,second_carrier8,price_t1]
	second_carriers4=[second_carrier9,second_carrier10,second_carrier11,price_t1]
	second_carriers5=[second_carrier12,second_carrier13,second_carrier14,price_t1]
	second_carriers6=[second_carrier15,second_carrier16,second_carrier17,price_t1]
	second_carriers7=[second_carrier18,second_carrier19,second_carrier20,price_t1]
	second_carriers8=[second_carrier21,second_carrier22,second_carrier23,price_t1]
	layovers1=[layover0,layover1,layover2,eurail_info[0]]
	layovers2=[layover3,layover4,layover5,eurail_info[1]]
	layovers3=[layover6,layover7,layover8,eurail_info[2]]
	layovers4=[layover9,layover10,layover11,eurail_info[3]]
	layovers5=[layover12,layover13,layover14,eurail_info[4]]
	layovers6=[layover15,layover16,layover17,eurail_info[5]]
	layovers7=[layover18,layover19,layover20,eurail_info[6]]
	layovers8=[layover21,layover22,layover23,eurail_info[7]]

	result_st2=result_st[1:]
	global kkk
	kkk=[]
	kkk=[zip(prices1,stops1,carriers1,carriers2_1,arrivaltimes1,departuretimes1,durations1,radios1,second_departuretimes1,second_arrivaltimes1,second_durations1,second_carriers1,layovers1),zip(prices2,stops2,carriers2,carriers2_2,arrivaltimes2,departuretimes2,durations2,radios2,second_departuretimes2,second_arrivaltimes2,second_durations2,second_carriers2,layovers2),zip(prices3,stops3,carriers3,carriers2_3,arrivaltimes3,departuretimes3,durations3,radios3,second_departuretimes3,second_arrivaltimes3,second_durations3,second_carriers3,layovers3),zip(prices4,stops4,carriers4,carriers2_4,arrivaltimes4,departuretimes4,durations4,radios4,second_departuretimes4,second_arrivaltimes4,second_durations4,second_carriers4,layovers4),zip(prices5,stops5,carriers5,carriers2_5,arrivaltimes5,departuretimes5,durations5,radios5,second_departuretimes5,second_arrivaltimes5,second_durations5,second_carriers5,layovers5),zip(prices6,stops6,carriers6,carriers2_6,arrivaltimes6,departuretimes6,durations6,radios6,second_departuretimes6,second_arrivaltimes6,second_durations6,second_carriers6,layovers6),zip(prices7,stops7,carriers7,carriers2_7,arrivaltimes7,departuretimes7,durations7,radios7,second_departuretimes7,second_arrivaltimes7,second_durations7,second_carriers7,layovers7),zip(prices8,stops8,carriers8,carriers2_8,arrivaltimes8,departuretimes8,durations8,radios8,second_departuretimes8,second_arrivaltimes8,second_durations8,second_carriers8,layovers8)]

	global location_real
	location_real=[]
	for i in result_air3:
	   a=airport_all.index(i)
	   location_real.append(location_all[a-1])

	global first_dep
	first_dep=[]
  	c=airport_all.index(result_air3[0])
	first_dep=location_all[c-1]

	global air_result_kor   
	air_result_kor = []
   	for i in result_air3:
		air_kor_name = models.Airport.objects.get(air_name = i)
		air_result_kor.append(air_kor_name.city_name)

	global results2, results3
	results2=[]
	results3=[]	
	results2=zip(air_result_kor,result_st2)
	results3=zip(air_result_kor,result_st2,result_air3)

	return render(request, 'pages/result.html', {"adult_num": adult_num,
												 "kid_num": kid_num,
												 "depday": depday,
												 "arrday": arrday,
												 "location_real":location_real,
												 "result_air":result_air,
											     "kkk": kkk,
											     "real_air":real_air,
											     "results2":results2,
											     "result_air3":result_air3,
											     "air_result_kor" : air_result_kor,
											     "results3":results3,
											     "lastcity":lastcity,
											     "first_dep":first_dep,
												 })

def desearch(request):
	conn = sqlite3.connect("lapistadb.db")
	try:
		my_list = models.Mylist.objects.get(list_id=str(list_id))
	except models.Mylist.DoesNotExist:
		my_list = None
	


	result_st=[]
	result_air=[]
	
	for a in ori1:
		result_air.append(str(a))
	result_air.append('ICN')
	result_dep=[0]*len(ori1)
	for j in range(len(li_de_dep)):
		if len(li_de_dep[j])>=11:
			result_dep[j]=str(li_de_dep[j][:4])+str('-')+str(li_de_dep[j][6:8])+str('-')+str(li_de_dep[j][10:12])

		else:
			result_dep[j]=str(li_de_dep[j])
	print(result_air)
	print(result_dep)


	response = [0]*(len(result_dep))
	api_key= [0]*(len(result_dep))
	url=[0]*(len(result_dep))
	headers=[0]*(len(result_dep))
	params=[0]*(len(result_dep))

	# api_key="AIzaSyDbpKpdqdIlItEhipc0j6fATk4iHaWdzUw"
	api_key = "AIzaSyDiYhxOy8UR29FtgCQHsZz_7yxRkIrVK_E"
	url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
	headers = {'content-type': 'application/json'}
	global prices
	prices=[]
	stops=[]
	carriers=[]
	carriers_2=[]
	arrivaltimes = []
	departuretimes = []
	durations = []
	second_arrivaltimes=[]
	second_departuretimes = []
	second_durations = []
	second_carriers = []
	layovers = []

	for i in range(len(result_dep)):
		params = {
			"request": {
					"slice": [
						{
						"origin": result_air[i],
						"destination": result_air[i+1],
						"date": result_dep[i],
						"maxStops": 1,
						# "maxConnectionDuration": 5000,
					}
				],
				"passengers": {
					"adultCount": 1,
					"childCount": 0,
				},
				"solutions": 30,
				# "refundable": False,
				"saleCountry": "US",
			}
		}
		response = requests.post(url, data=json.dumps(params), headers=headers)
		data = response.json()

		price = [0]*3
		stop = [0]*3
		Carrier = [0]*3
		Carriersss = [0]*3
		arrivaltime = [0]*3
		departuretime = [0]*3
		duration = [0]*3
		second_arrivaltime=[0]*3
		second_departuretime = [0]*3
		second_duration = [0]*3
		layover = [0]*3
		durationhour = [0]*3
		durationminute = [0]*3
		second_durationhour = [0]*3
		second_durationminute = [0]*3
		stophour = [0]*3
		stopminute = [0]*3
		second_carrier = [0]*3
		for j in range(3):
			price[j] = data["trips"]["tripOption"][j]["saleTotal"]
			stop[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0].get("connectionDuration", 20000)
			if stop[j] != 20000:	
				second_arrivaltime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["arrivalTime"]
				second_departuretime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["departureTime"]
				second_duration[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["leg"][0]["duration"]
				second_carrier[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["flight"]["carrier"]+data["trips"]["tripOption"][j]["slice"][0]["segment"][1]["flight"]["number"]
				layover[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["destination"]
		
			else:
				second_arrivaltime[j] = 0
				second_departuretime[j] = 0
				second_duration[j] = 0
				second_carrier[j] = 0
				layover[j] = 0

			Carrier[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["flight"]["carrier"]+data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["flight"]["number"]
			Carriersss[j]= data["trips"]["data"]["carrier"][j]["name"]
			arrivaltime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["arrivalTime"]
			if int(arrivaltime[j][11:13])< 12 :
			    t=arrivaltime[j][11:13]+':' +arrivaltime[j][14:16]+' AM'

			elif int(arrivaltime[j][11:13])== 13 :
			    t=arrivaltime[j][11:13]+':' +arrivaltime[j][14:16]+' PM'     

			else :
				t='0'+str(int(arrivaltime[j][11:13])-12)+':' +arrivaltime[j][14:16]+' PM'
			arrivaltime[j]= arrivaltime[j][:4]+'년'+' '+arrivaltime[j][5:7]+'월'+' '+arrivaltime[j][8:10]+'일'+' '+t

			departuretime[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["departureTime"]
			if int(departuretime[j][11:13])< 12 :
			    print(departuretime[j][11:13])
			    t=departuretime[j][11:13]+':' +departuretime[j][14:16]+' AM'

			elif int(departuretime[j][11:13])== 13 :
			    print(departuretime[j][11:13])
			    t=departuretime[j][11:13]+':' +departuretime[j][14:16]+' PM'  

			else :
				t='0'+str(int(departuretime[j][11:13])-12)+':' +departuretime[j][14:16]+' PM'
			departuretime[j]= departuretime[j][:4]+'년'+' '+departuretime[j][5:7]+'월'+' '+departuretime[j][8:10]+'일'+' '+t

			if stop[j] != 20000:
				if int(second_arrivaltime[j][11:13])< 12 :
				    t=second_arrivaltime[j][11:13]+':' +second_arrivaltime[j][14:16]+' AM'

				elif int(second_arrivaltime[j][11:13])== 13 :
				    t=second_arrivaltime[j][11:13]+':' +second_arrivaltime[j][14:16]+' PM'  

				else :
					t='0'+str(int(second_arrivaltime[j][11:13])-12)+':' +second_arrivaltime[j][14:16]+' PM'
				second_arrivaltime[j] = second_arrivaltime[j][:4]+'년'+' '+second_arrivaltime[j][5:7]+'월'+' '+second_arrivaltime[j][8:10]+'일'+' '+t

				if int(second_departuretime[j][11:13])< 12 :
				    print(second_departuretime[j][11:13])
				    t=second_departuretime[j][11:13]+':' +second_departuretime[j][14:16]+' AM'

				elif int(second_departuretime[j][11:13])== 13 :
				    print(second_departuretime[j][11:13])
				    t=second_departuretime[j][11:13]+':' +second_departuretime[j][14:16]+' PM' 

				else :
					t='0'+str(int(second_departuretime[j][11:13])-12)+':' +second_departuretime[j][14:16]+' PM'
				second_departuretime[j]= second_departuretime[j][:4]+'년'+' '+second_departuretime[j][5:7]+'월'+' '+second_departuretime[j][8:10]+'일'+' '+t
				
			

			duration[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]

			durationhour[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]//60
			durationminute[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["leg"][0]["duration"]%60
			if durationhour[j] < 10:
				durationhour[j]=str(0)+str(durationhour[j])
			if durationminute[j] < 10:
				durationminute[j] = str(0) + str(durationminute[j])
			duration[j] = str(durationhour[j])+"시간 "+str(durationminute[j])+"분 "

			second_durationhour[j] = second_duration[j]//60
			second_durationminute[j] = second_duration[j]%60
			if second_durationhour[j] < 10:
				durationhour[j]=str(0)+str(second_durationhour[j])
			if second_durationminute[j] < 10:
				second_durationminute[j] = str(0) + str(second_durationminute[j])
			second_duration[j] = str(second_durationhour[j])+"시간 "+str(second_durationminute[j])+"분 "

			if stop[j] != 20000:
				stophour[j] = stop[j]//60
				stopminute[j] =stop[j]%60
				if stophour[j] < 10:
					stophour[j]=str(0)+str(stophour[j])
				if stopminute[j] < 10:
					stopminute[j] = str(0) + str(stopminute[j])
				stop[j] = " "+str(stophour[j])+"시간 "+str(stopminute[j])+"분 "

				print(stop)

			prices.append(str(price[j]))
			stops.append(stop[j])
			carriers.append(Carrier[j])
			carriers_2.append(Carriersss[j])
			arrivaltimes.append(arrivaltime[j])
			departuretimes.append(departuretime[j])
			durations.append(duration[j])
			second_arrivaltimes.append(second_arrivaltime[j])
			second_departuretimes.append(second_departuretime[j])
			second_durations.append(second_duration[j])
			second_carriers.append(second_carrier[j])
			layovers.append(layover[j])

	real_price =[]	
	real_stop =[]
	real_carrier =[]
	real_carrier2 =[]
	real_arrivaltime = []
	real_departuretime = []
	real_duration = []
	real_radio=[]
	real_second_arrivaltime = []
	real_second_departuretime= []
	real_second_duration = []
	real_second_carrier = []
	real_layover = []
	for i in range(24):
		real_price.append(str("price")+str(i))
		real_stop.append(str("stop")+str(i))
		real_carrier.append(str("carrier")+str(i))
		real_carrier2.append(str("carrier2_")+str(i))
		real_arrivaltime.append(str("arrivaltime")+str(i))
		real_departuretime.append(str("departuretime")+str(i))
		real_duration.append(str("duration")+str(i))
		real_second_arrivaltime.append(str("second_arrivaltime")+str(i))
		real_second_departuretime.append(str("second_departuretime")+str(i))
		real_second_duration.append(str("second_duration")+str(i))
		real_second_carrier.append(str("second_carrier")+str(i))
		real_layover.append(str("layover")+str(i))

	for i in range(32):	
		real_radio.append(str("radio")+str(i))	

	for i in range(len(real_price)-len(prices)):
		prices.append(0)
		stops.append(0)
		carriers.append(0)
		carriers_2.append(0)
		arrivaltimes.append(0)
		departuretimes.append(0)
		durations.append(0)
		second_arrivaltimes.append(0)
		second_departuretimes.append(0)
		second_durations.append(0)
		second_carriers.append(0)
		layovers.append(0)

	radios=[]    
	for i in range(8):
		radios.append(str("radio")+str(i))
	radios=radios*4
	radios.sort()

	for i in zip(real_radio,radios):	
		globals()[i[0]]=i[1]


	for i in zip(real_price,prices,real_stop,stops,real_carrier,carriers,real_carrier2,carriers_2,real_arrivaltime,arrivaltimes,real_departuretime,departuretimes,real_duration,durations,real_second_arrivaltime,second_arrivaltimes,real_second_departuretime,second_departuretimes,real_second_duration,second_durations,real_second_carrier,second_carriers,real_layover,layovers):
		if i[1] != 0:
			globals()[i[0]]=float(i[1][3:])
			globals()[i[2]]=i[3]
			globals()[i[4]]=i[5]
			globals()[i[6]]=i[7]
			globals()[i[8]]=i[9]
			globals()[i[10]]=i[11]
			globals()[i[12]]=i[13]
			globals()[i[14]]=i[15]
			globals()[i[16]]=i[17]
			globals()[i[18]]=i[19]
			globals()[i[20]]=i[21]
			globals()[i[22]]=i[23]
		else:
			globals()[i[0]]=i[1]
			globals()[i[2]]=i[3]
			globals()[i[4]]=i[5]
			globals()[i[6]]=i[7]
			globals()[i[8]]=i[9]
			globals()[i[10]]=i[11]
			globals()[i[12]]=i[13]
			globals()[i[14]]=i[15]
			globals()[i[16]]=i[17]
			globals()[i[18]]=i[19]
			globals()[i[20]]=i[21]
			globals()[i[22]]=i[23]

	conn = sqlite3.connect("lapistadb.db")
	eurail_cost = []
	eurail_dep = []
	eurail_arr = []
	eurail_time = []
	e_dep_date = []
	for i in range(len(result_air) - 1):
		cursor3 = conn.execute(
			"SELECT PRICE,DEP_TIME,ARR_TIME,REQUIRED_TIME from eurail where dep_date=(?) and r_origin=(?) and r_dest=(?)",
			(result_dep[i], result_air[i], result_air[i + 1]))
		eurail_cost.append([])
		eurail_dep.append([])
		eurail_arr.append([])
		eurail_time.append([])
		e_dep_date.append(result_dep[i])
		for row in cursor3:
			eurail_cost[i].append(row[0])
			eurail_dep[i].append(row[1])
			eurail_arr[i].append(row[2])
			eurail_time[i].append(row[3])
		else:
			eurail_cost[i].append(0)
			eurail_dep[i].append(0)
			eurail_arr[i].append(0)
			eurail_time[i].append(0)

	while len(e_dep_date) != 8:
		e_dep_date.append(0)		

	eurail_top_c = [0] * 8
	for i in range(len(eurail_cost)):
		for j in range(len(eurail_cost[i])):
			eurail_top_c[i] = eurail_cost[i][0]

	eurail_top_d = [0] * 8
	for i in range(len(eurail_dep)):
		for j in range(len(eurail_dep[i])):
			eurail_top_d[i] = eurail_dep[i][0]

	eurail_top_a = [0] * 8
	for i in range(len(eurail_arr)):
		for j in range(len(eurail_arr[i])):
			eurail_top_a[i] = eurail_arr[i][0]

	eurail_top_t = [0] * 8
	for i in range(len(eurail_time)):
		for j in range(len(eurail_time[i])):
			eurail_top_t[i] = eurail_time[i][0]

	eurail_info = ['유레일스케쥴'] * 8
	for i in range(len(eurail_cost)):
		for j in range(len(eurail_cost[i])):
			if eurail_cost[i][j] != 0:
				a = '$' + str(eurail_cost[i][j]) + ' ' + str(eurail_dep[i][j]) + ' ' + str(eurail_time[i][j])
				eurail_info[i] = ''.join((eurail_info[i], a))
	print(eurail_info)

	Eurail = 'Eurail'
	price_t1=[22,34,55]
	price_t2=0
	prices1=[price0,price1,price2,eurail_top_c[0]]
	prices2=[price3,price4,price5,eurail_top_c[1]]
	prices3=[price6,price7,price8,eurail_top_c[2]]
	prices4=[price9,price10,price11,eurail_top_c[3]]
	prices5=[price12,price13,price14,eurail_top_c[4]]
	prices6=[price15,price16,price17,eurail_top_c[5]]
	prices7=[price18,price19,price20,eurail_top_c[6]]
	prices8=[price21,price22,price23,eurail_top_c[7]]
	global price_all
	price_all=[prices1,prices2,prices3,prices4,prices5,prices6,prices7,prices8]
	stops1=[stop0,stop1,stop2,eurail_info[0]]
	stops2=[stop3,stop4,stop5,eurail_info[1]]
	stops3=[stop6,stop7,stop8,eurail_info[2]]
	stops4=[stop9,stop10,stop11,eurail_info[3]]
	stops5=[stop12,stop13,stop14,eurail_info[4]]
	stops6=[stop15,stop16,stop17,eurail_info[5]]
	stops7=[stop18,stop19,stop20,eurail_info[6]]
	stops8=[stop21,stop22,stop23,eurail_info[7]]
	carriers1=[carrier0,carrier1,carrier2,Eurail]
	carriers2=[carrier3,carrier4,carrier5,Eurail]
	carriers3=[carrier6,carrier7,carrier8,Eurail]
	carriers4=[carrier9,carrier10,carrier11,Eurail]
	carriers5=[carrier12,carrier13,carrier14,Eurail]
	carriers6=[carrier15,carrier16,carrier17,Eurail]
	carriers7=[carrier18,carrier19,carrier20,Eurail]
	carriers8=[carrier21,carrier22,carrier23,Eurail]
	carriers2_1=[carrier2_0,carrier2_1,carrier2_2,Eurail]
	carriers2_2=[carrier2_3,carrier2_4,carrier2_5,Eurail]
	carriers2_3=[carrier2_6,carrier2_7,carrier2_8,Eurail]
	carriers2_4=[carrier2_9,carrier2_10,carrier2_11,Eurail]
	carriers2_5=[carrier2_12,carrier2_13,carrier2_14,Eurail]
	carriers2_6=[carrier2_15,carrier2_16,carrier2_17,Eurail]
	carriers2_7=[carrier2_18,carrier2_19,carrier2_20,Eurail]
	carriers2_8=[carrier2_21,carrier2_22,carrier2_23,Eurail]
	arrivaltimes1=[arrivaltime0,arrivaltime1,arrivaltime2,eurail_top_a[0]]
	arrivaltimes2=[arrivaltime3,arrivaltime4,arrivaltime5,eurail_top_a[1]]
	arrivaltimes3=[arrivaltime6,arrivaltime7,arrivaltime8,eurail_top_a[2]]
	arrivaltimes4=[arrivaltime9,arrivaltime10,arrivaltime11,eurail_top_a[3]]
	arrivaltimes5=[arrivaltime12,arrivaltime13,arrivaltime14,eurail_top_a[4]]
	arrivaltimes6=[arrivaltime15,arrivaltime16,arrivaltime17,eurail_top_a[5]]
	arrivaltimes7=[arrivaltime18,arrivaltime19,arrivaltime20,eurail_top_a[6]]
	arrivaltimes8=[arrivaltime21,arrivaltime22,arrivaltime23,eurail_top_a[7]]
	departuretimes1=[departuretime0,departuretime1,departuretime2,e_dep_date[0]]
	departuretimes2=[departuretime3,departuretime4,departuretime5,e_dep_date[1]]
	departuretimes3=[departuretime6,departuretime7,departuretime8,e_dep_date[2]]
	departuretimes4=[departuretime9,departuretime10,departuretime11,e_dep_date[3]]
	departuretimes5=[departuretime12,departuretime13,departuretime14,e_dep_date[4]]
	departuretimes6=[departuretime15,departuretime16,departuretime17,e_dep_date[5]]
	departuretimes7=[departuretime18,departuretime19,departuretime20,e_dep_date[6]]
	departuretimes8=[departuretime21,departuretime22,departuretime23,e_dep_date[7]]
	durations1=[duration0,duration1,duration2,eurail_top_t[0]]
	durations2=[duration3,duration4,duration5,eurail_top_t[1]]
	durations3=[duration6,duration7,duration8,eurail_top_t[2]]
	durations4=[duration9,duration10,duration11,eurail_top_t[3]]
	durations5=[duration12,duration13,duration14,eurail_top_t[4]]
	durations6=[duration15,duration16,duration17,eurail_top_t[5]]
	durations7=[duration18,duration19,duration20,eurail_top_t[6]]
	durations8=[duration21,duration22,duration23,eurail_top_t[7]]
	radios1=[radio0,radio1,radio2,radio3]
	radios2=[radio4,radio5,radio6,radio7]
	radios3=[radio8,radio9,radio10,radio11]
	radios4=[radio12,radio13,radio14,radio15]
	radios5=[radio16,radio17,radio18,radio19]
	radios6=[radio20,radio21,radio22,radio23]
	radios7=[radio24,radio25,radio26,radio27]
	radios8=[radio28,radio29,radio30,radio31]
	second_arrivaltimes1=[second_arrivaltime0,second_arrivaltime1,second_arrivaltime2,price_t1]
	second_arrivaltimes2=[second_arrivaltime3,second_arrivaltime4,second_arrivaltime5,price_t1]
	second_arrivaltimes3=[second_arrivaltime6,second_arrivaltime7,second_arrivaltime8,price_t1]
	second_arrivaltimes4=[second_arrivaltime9,second_arrivaltime10,second_arrivaltime11,price_t2]
	second_arrivaltimes5=[second_arrivaltime12,second_arrivaltime13,second_arrivaltime14,price_t2]
	second_arrivaltimes6=[second_arrivaltime15,second_arrivaltime16,second_arrivaltime17,price_t2]
	second_arrivaltimes7=[second_arrivaltime18,second_arrivaltime19,second_arrivaltime20,price_t2]
	second_arrivaltimes8=[second_arrivaltime21,second_arrivaltime22,second_arrivaltime23,price_t2]
	second_departuretimes1=[second_departuretime0,second_departuretime1,second_departuretime2,price_t1]
	second_departuretimes2=[second_departuretime3,second_departuretime4,second_departuretime5,price_t1]
	second_departuretimes3=[second_departuretime6,second_departuretime7,second_departuretime8,price_t1]
	second_departuretimes4=[second_departuretime9,second_departuretime10,second_departuretime11,price_t2]
	second_departuretimes5=[second_departuretime12,second_departuretime13,second_departuretime14,price_t2]
	second_departuretimes6=[second_departuretime15,second_departuretime16,second_departuretime17,price_t2]
	second_departuretimes7=[second_departuretime18,second_departuretime19,second_departuretime20,price_t2]
	second_departuretimes8=[second_departuretime21,second_departuretime22,second_departuretime23,price_t2]
	second_durations1=[second_duration0,second_duration1,second_duration2,price_t1]
	second_durations2=[second_duration3,second_duration4,second_duration5,price_t1]
	second_durations3=[second_duration6,second_duration7,second_duration8,price_t1]
	second_durations4=[second_duration9,second_duration10,second_duration11,price_t2]
	second_durations5=[second_duration12,second_duration13,second_duration14,price_t2]
	second_durations6=[second_duration15,second_duration16,second_duration17,price_t2]
	second_durations7=[second_duration18,second_duration19,second_duration20,price_t2]
	second_durations8=[second_duration21,second_duration22,second_duration23,price_t2]
	second_carriers1=[second_carrier0,second_carrier1,second_carrier2,price_t1]
	second_carriers2=[second_carrier3,second_carrier4,second_carrier5,price_t1]
	second_carriers3=[second_carrier6,second_carrier7,second_carrier8,price_t1]
	second_carriers4=[second_carrier9,second_carrier10,second_carrier11,price_t1]
	second_carriers5=[second_carrier12,second_carrier13,second_carrier14,price_t1]
	second_carriers6=[second_carrier15,second_carrier16,second_carrier17,price_t1]
	second_carriers7=[second_carrier18,second_carrier19,second_carrier20,price_t1]
	second_carriers8=[second_carrier21,second_carrier22,second_carrier23,price_t1]
	layovers1=[layover0,layover1,layover2,eurail_info[0]]
	layovers2=[layover3,layover4,layover5,eurail_info[1]]
	layovers3=[layover6,layover7,layover8,eurail_info[2]]
	layovers4=[layover9,layover10,layover11,eurail_info[3]]
	layovers5=[layover12,layover13,layover14,eurail_info[4]]
	layovers6=[layover15,layover16,layover17,eurail_info[5]]
	layovers7=[layover18,layover19,layover20,eurail_info[6]]
	layovers8=[layover21,layover22,layover23,eurail_info[7]]

	result_st2=result_st[1:]
	global kkk
	kkk=[]
	kkk=[zip(prices1,stops1,carriers1,carriers2_1,arrivaltimes1,departuretimes1,durations1,radios1,second_departuretimes1,second_arrivaltimes1,second_durations1,second_carriers1,layovers1),zip(prices2,stops2,carriers2,carriers2_2,arrivaltimes2,departuretimes2,durations2,radios2,second_departuretimes2,second_arrivaltimes2,second_durations2,second_carriers2,layovers2),zip(prices3,stops3,carriers3,carriers2_3,arrivaltimes3,departuretimes3,durations3,radios3,second_departuretimes3,second_arrivaltimes3,second_durations3,second_carriers3,layovers3),zip(prices4,stops4,carriers4,carriers2_4,arrivaltimes4,departuretimes4,durations4,radios4,second_departuretimes4,second_arrivaltimes4,second_durations4,second_carriers4,layovers4),zip(prices5,stops5,carriers5,carriers2_5,arrivaltimes5,departuretimes5,durations5,radios5,second_departuretimes5,second_arrivaltimes5,second_durations5,second_carriers5,layovers5),zip(prices6,stops6,carriers6,carriers2_6,arrivaltimes6,departuretimes6,durations6,radios6,second_departuretimes6,second_arrivaltimes6,second_durations6,second_carriers6,layovers6),zip(prices7,stops7,carriers7,carriers2_7,arrivaltimes7,departuretimes7,durations7,radios7,second_departuretimes7,second_arrivaltimes7,second_durations7,second_carriers7,layovers7),zip(prices8,stops8,carriers8,carriers2_8,arrivaltimes8,departuretimes8,durations8,radios8,second_departuretimes8,second_arrivaltimes8,second_durations8,second_carriers8,layovers8)]
	global location_real
	location_real=location_detail

	return render(request, 'pages/desearch.html', {"location_real":location_real,
												 "result_air":result_air,
											     "kkk": kkk,
											     "my_list": my_list,
											     "air_result_kor": li_de_origin_kor,
											     "results2": big_zip,
											     "real_air": li_de_zip,
											     "location_detail": location_detail,
											     "first_dep": first_dep,
												 })


def course(request):
	return render(request, 'pages/course.html')

def explain(request):
	return render(request, 'pages/explain.html')

def final(request):
	return render(request, 'pages/final.html')	

def list(request):

	air_picture_final = []

	my_all_list = models.Mylist.objects.filter(username=request.user)
	detail_city = my_all_list.values_list('city_1', 'city_2', 'city_3', 'city_4', 'city_5', 'city_6', 'city_7',
										  'city_8')

	for i in range(my_all_list.count()):
		remove_none = filter(None, detail_city[i])
		air_list_picture = []
		for j in remove_none:
			air_picture = models.Airport.objects.get(air_name=str(j))
			air_list_picture.append(air_picture.coun_pic)
		air_picture_final.append(air_list_picture)
	detail_zip = zip(my_all_list, air_picture_final)

	return render(request, 'pages/list.html',
        {'detail_zip':detail_zip}
				  )
    
def detail(request):
    #-*- coding: utf-8 -*-
    global list_id,my_list
    list_id=request.POST.get("listid")
    my_list = models.Mylist.objects.get(list_id=list_id)
    conn = sqlite3.connect("lapistadb.db")
    global li_de_dep
    li_de_cost = []
    li_de_stop = []
    li_de_arr = []
    li_de_dep = []
    li_de_duration1 = []
    li_de_second_dep = []
    li_de_second_arr = []
    li_de_duration2 = []
    li_de_layover=[]
    li_de_routeid = []
    li_de_trendep = []
    cursor3 = conn.execute("SELECT cost,stop_num,arr_date,dep_date,flight_time,second_dep,second_arr,second_duration,layover,route_id,dep_time from listdetail where list_id=(?)", (list_id,))
    
    for row in cursor3:
        li_de_cost.append(row[0])
        li_de_stop.append(row[1])
        li_de_arr.append(row[2])
        li_de_dep.append(row[3])
        li_de_duration1.append(row[4])
        li_de_second_dep.append(row[5])
        li_de_second_arr.append(row[6])
        li_de_duration2.append(row[7])
        li_de_layover.append(row[8])
        li_de_routeid.append(row[9])
        li_de_trendep.append(row[10])
    li_de_origin1 = []
    li_de_origin1.append(my_list.city_1),li_de_origin1.append(my_list.city_2),
    li_de_origin1.append(my_list.city_3),li_de_origin1.append(my_list.city_4),
    li_de_origin1.append(my_list.city_5),li_de_origin1.append(my_list.city_6),
    li_de_origin1.append(my_list.city_7),li_de_origin1.append(my_list.city_8)
    li_de_stay = []
    li_de_stay.append(my_list.stay_1),li_de_stay.append(my_list.stay_2),
    li_de_stay.append(my_list.stay_3),li_de_stay.append(my_list.stay_4),
    li_de_stay.append(my_list.stay_5),li_de_stay.append(my_list.stay_6),
    li_de_stay.append(my_list.stay_7),li_de_stay.append(my_list.stay_8)
    remove_none2 = filter(None, li_de_origin1)
    maplist = [x.encode('UTF8') for x in remove_none2]
    list_num = len(remove_none2)
    global airport_all
    airport_all=['ICN','FCO','CDG','LHR','MAD','SXF','BRU','FRA','MUC','AMS','DUB','KRK','WAW','BOJ','SOF','NCE','BUD','PRG','LIS','OTP','ZRH','BCN']
    lhr_loc={}
    lhr_loc['lat']=51.27159
    lhr_loc['lng']=-0.20443
    
    cdg_loc={}
    cdg_loc['lat']=48.646
    cdg_loc['lng']=2.330
    mad_loc={}
    mad_loc['lat']=40.5
    mad_loc['lng']=-3.567
    fco_loc={}
    fco_loc['lat']=41.8
    fco_loc['lng']=12.25
    sxf_loc={}
    sxf_loc['lat']=52.56
    sxf_loc['lng']=13.29
    bru_loc={}
    bru_loc['lat']=50.900755
    bru_loc['lng']=4.479653
    fra_loc={}
    fra_loc['lat']=50.038105
    fra_loc['lng']=8.562474
    muc_loc={}
    muc_loc['lat']=48.358051
    muc_loc['lng']=11.784187
    ams_loc={}
    ams_loc['lat']=52.310834
    ams_loc['lng']=4.768071
    dub_loc={}
    dub_loc['lat']=53.426646
    dub_loc['lng']=-6.250135
    krk_loc={}
    krk_loc['lat']=50.077095
    krk_loc['lng']=19.787271
    waw_loc={}
    waw_loc['lat']=52.167526
    waw_loc['lng']=20.967440
    boj_loc={}
    boj_loc['lat']=42.565492
    boj_loc['lng']=27.516538
    sof_loc={}
    sof_loc['lat']=42.689235
    sof_loc['lng']=23.414747
    nce_loc={}
    nce_loc['lat']=43.660048
    nce_loc['lng']=7.214049
    bud_loc={}
    bud_loc['lat']=47.438604
    bud_loc['lng']=19.251588
    prg_loc={}
    prg_loc['lat']=50.102101
    prg_loc['lng']=14.262849
    lis_loc={}
    lis_loc['lat']=38.775953
    lis_loc['lng']=-9.135495
    otp_loc={}
    otp_loc['lat']=44.571227
    otp_loc['lng']=26.084412
    zrh_loc={}
    zrh_loc['lat']=47.458362
    zrh_loc['lng']=8.554821
    bcn_loc={}
    bcn_loc['lat']=41.297308
    bcn_loc['lng']=2.082811
    global location_all
    location_all=[fco_loc,cdg_loc,lhr_loc,mad_loc,sxf_loc,bru_loc,fra_loc,muc_loc,ams_loc,dub_loc,krk_loc,waw_loc,boj_loc,sof_loc,nce_loc,bud_loc,prg_loc,lis_loc,otp_loc,zrh_loc,bcn_loc]
    global location_detail
    location_detail=[]
    for i in maplist:
        a=airport_all.index(i)
        location_detail.append(location_all[a-1])
    b=airport_all.index(maplist[0])

    global first_dep
    first_dep=location_all[b-1]
    global li_de_origin_kor
    li_de_origin_kor = []
    li_de_origin_eng =[]
    for j in remove_none2:
        origin_kor = models.Airport.objects.get(air_name=j)
        li_de_origin_kor.append(origin_kor.city_name)
        origin_eng = models.Airport.objects.get(air_name=j)
        li_de_origin_eng.append(origin_eng.city_eng)
    li_de_stay_final = filter(None, li_de_stay)
    print(li_de_stay_final)
    global ori1
    ori1 = ['ICN']
    for i in remove_none2 :
        ori1.append(i)
    ori2 = []
    for i in remove_none2 :
        ori2.append(i)
    ori2.append('ICN')
    timenow = date.today()
    savedate=my_list.save_date
    trendresult = []
    text = []
    trend_zip = zip(li_de_routeid, li_de_trendep)
    for j,i in trend_zip:
        a = datetime.strptime(i, '%Y-%m-%d').date() - savedate
        b = datetime.strptime(i, '%Y-%m-%d').date() - timenow
        a = a.days
        b = b.days
        print(datetime.strptime(i, '%Y-%m-%d').date())
        trendroute = models.Trend.objects.filter(route_id = j)
        choosesavetrend = trendroute.get(daysleft = a)
        choosenowtrend = trendroute.get(daysleft = b)
        if choosenowtrend > choosesavetrend :
            trendresult.append('/static/추세1.png')
            text.append("LaPista의 추세모형을 이용한 결과 7일 이내에 가격이 상승할 예정입니다. 서둘러 예매하세요 :)")
        elif choosenowtrend < choosesavetrend :
            trendresult.append('/static/추세2.png')
            text.append("LaPista의 추세모형을 이용한 결과 7일 이내에 가격이 하락할 예정입니다. 조금만 기다려보세요 :)")
    dep_cut=[]        
    for i in li_de_dep:
        dep_cut.append(i[0:13])        
    global big_zip        
    big_zip = zip(li_de_origin_kor, li_de_stay_final)

    my_dep =[]
    for i in range(len(li_de_trendep)):
        my_dep.append(str(li_de_trendep[i]))

    global li_de_zip
    li_de_zip = zip(li_de_cost,li_de_stop,li_de_arr,li_de_dep,li_de_duration1,li_de_second_dep,li_de_second_arr,li_de_duration2,li_de_layover, ori1,ori2,trendresult,text,dep_cut,my_dep)
    menus={}
    menus2=[]
    for i in li_de_origin_kor:
       h=[]
       for k in range(0,3):
          
       	 a = i + str(k+1)
         h.append(a)
         menus2.append(a)
       menus[i] = h
    print(menus)
    tab_pic_final = []
    for i in remove_none2:
        tab_preview = models.Airport.objects.get(air_name=str(i))
        tab_pic_final.append(tab_preview.city_info1)
        tab_pic_final.append(tab_preview.city_info2)
        tab_pic_final.append(tab_preview.city_info3)
    print(tab_pic_final)
                # menus2.append(a)
                # menus2.append(b)
        # a = i + str(result_st[li_de_origin_kor.index(i)]) 
        # b = i + str(result_st[li_de_origin_kor.index(i)]+1)
    print(li_de_origin_eng)
    event = []
    color =['#F08080 ','#191970 ','#9370DB ','#DB7093 ','#483D8B ','red','#4169E1 ']
    print(li_de_trendep)
    for i in range(len(li_de_trendep)-1):
        a={}
        a['title'] = str(li_de_origin_eng[i])
        a['start'] = str(li_de_trendep[i])
        k= datetime.strptime(str(li_de_trendep[i]), '%Y-%m-%d').date()
        print(k,type(k))
        k2 = k.toordinal()+int(str(li_de_stay_final[i]))
        print(k2)
        k3= str(datetime.fromordinal(k2))
        a['end'] = k3[:10]
        a['color']=color[i]
        print(k3[:10])
        event.append(a)
    print(event)
    print(menus2)
    print(menus)
    tab_zip = zip(menus2,tab_pic_final)
    print(tab_zip)
    return render(request, 'pages/detail.html', {"menus":menus , "menus2":menus2,"my_list":my_list,
        "li_de_zip": li_de_zip, "big_zip":big_zip , "event":event, "location_detail":location_detail,"first_dep":first_dep,"savedate":savedate,"tab_zip":tab_zip,"list_num":list_num})
    return JsonResponse(event,safe=False)

def geo(request):
	result_air3=['FCO','CDG','MAD']
	fco_loc={}
	fco_loc={'lat':36.05,'lng':27.33}

	lhr_loc={}
	lhr_loc['lat']=51.27159
	lhr_loc['lng']=-0.20443
	
	cdg_loc={}
	cdg_loc['lat']=48.646
	cdg_loc['lng']=2.330

	mad_loc={}
	mad_loc['lat']=40.5
	mad_loc['lng']=-3.547

	airport_all=['FCO','CDG','LHR','MAD']
	location_all=[fco_loc,cdg_loc,lhr_loc,mad_loc]


	location_real=[]
	for i in result_air3:
	       a=airport_all.index(i)
	       location_real.append(location_all[a])

	junpark=  [
          {'lat': 37.772, 'lng': -122.214},
          {'lat': 21.291, 'lng': -157.821},
          {'lat': -18.142, 'lng': 178.431},
          {'lat': -27.467, 'lng': 153.027}
        ]

	return render(request, 'pages/geo.html',{"junpark":junpark,
											 "location_real":location_real})
def logo(request):
	return render(request, 'pages/logo.html')

def fordb(request):
	if request.method == 'POST':
		rradio=[0]*8
		radio2=['radio1','radio2','radio3','radio4','radio5','radio6']
		rradio[0] = request.POST.get('radio0')
		rradio[1] = request.POST.get('radio1')
		rradio[2] = request.POST.get('radio2')
		rradio[3] = request.POST.get('radio3')
		rradio[4] = request.POST.get('radio4')
		rradio[5] = request.POST.get('radio5')
		rradio[6] = request.POST.get('radio6')
		rradio[7] = request.POST.get('radio7')


		total_c = 0
		for i in range(len(result_air)-1):
			rradio[i] = float(rradio[i])
			a = price_all[i].index(rradio[i])
			total_c = total_c +kkk[i][a][0]

		while len(result_st) != 9:
			result_st.append(None)

		while len(result_air3) != 8:
			result_air3.append(None)

		new_mylist = models.Mylist.objects.create(dep_date=depday, total_cost = total_c,arr_date=arrday, username=request.user,
			stay_1=result_st[1], stay_2=result_st[2], stay_3=result_st[3],
			stay_4=result_st[4], stay_5=result_st[5], stay_6=result_st[6],
			stay_7=result_st[7], stay_8=result_st[8], city_1=result_air3[0],
			city_2=result_air3[1],city_3=result_air3[2], city_4=result_air3[3],
			city_5=result_air3[4], city_6=result_air3[5],city_7=result_air3[6],
			city_8=result_air3[7])

		my_list = models.Mylist.objects.latest('list_id')

		for i in range(len(result_air)-1):
			rradio[i] = float(rradio[i])
			a = price_all[i].index(rradio[i])

			routeroute = models.Route.objects.filter(r_origin=result_air[i])
			routeroute1 = routeroute.get(r_dest=result_air[i+1])

			new_detail = models.Listdetail.objects.create(list_id=my_list.list_id, cost=kkk[i][a][0],second_dep=kkk[i][a][8],
                                            second_arr=kkk[i][a][9], second_duration=kkk[i][a][10],dep_time=result_dep[i],
                                      airline=(kkk[i][a][3]), dep_date=kkk[i][a][5], r_origin=result_air[i], r_dest=result_air[i+1],
                                      arr_date=kkk[i][a][4], stop_num=kkk[i][a][1], flight_time=kkk[i][a][6],layover=kkk[i][a][12],
                                             route_id=routeroute1.route_id)

	return render(request, 'pages/fordb.html')

def trend(request):
	import datetime
	origin = request.GET.get("origin")
	origin1 = origin
	if origin is not None:
		destination = request.GET.get('destination')
		destination1 = destination
		dep=request.GET.get('dep')
		origin_air = models.Airport.objects.get(city_name=str(origin))
		origin = origin_air.air_name
		destination_air = models.Airport.objects.get(city_name=str(destination))
		destination = destination_air.air_name

	else:
		origin = 'ICN'
		destination ='CDG'
		destination1 = destination
		dep = '2017-06-30'
		print(origin)
		print(dep)

	conn = sqlite3.connect("lapistadb.db")
	#DEP = datetime.date(2017, 6, 4)
	dep=datetime.date(int(dep[:4]),int(dep[5:7]),int(dep[8:10]))
	DEP=dep
	TODAY = datetime.date.today()

	D1 = datetime.date.toordinal(DEP)
	D2 = (datetime.date.toordinal(TODAY))

	dates = []
	daysleft = []
	for i in range(D2, D1):
		dates.append(str(datetime.date.fromordinal(i)))
		daysleft.append(D1 - i)
		cursor = conn.execute("SELECT ROUTE_ID from route where r_origin=(?) and r_dest=(?)",(origin,destination))
	for row in cursor:
		route_i = str(row[0])

	scale_cost = []
	for j in daysleft:
		cursor2 = conn.execute("SELECT COST from trend where ROUTE_ID=(?) and daysleft=(?)", (route_i, j))
		for row in cursor2:
			scale_cost.append((float(row[0])))
	print(scale_cost)
	graph_cost = []
	for i in range(len(scale_cost)):
		graph_cost.append(int(scale_cost[i] / scale_cost[0] * 100))
		percent_cost=[i-100 for i in graph_cost]
	print(graph_cost)
	axis = []
	for i in range(len(scale_cost)):
		ax = {}
		ax["date"] = dates[i]
		ax["value"] = graph_cost[i]
		ax["value2"]=round(percent_cost[i])
		if graph_cost[i] is max(graph_cost):
			ax["color"]="#CC0000 "
			#ax["value2"]=round(percent_cost[i])
		elif graph_cost[i] is min(graph_cost):
			ax["color"]="#0054FF "
			#ax["value2"]=round(percent_cost[i])
			print(round(percent_cost[i]))
		axis.append(ax)
		min_date=dates[graph_cost.index(min(graph_cost))]
		max_date=dates[graph_cost.index(max(graph_cost))]
		max_price=max(graph_cost)-100

	return render(request, 'pages/trend.html',{"axis":axis,"min_date":min_date,"max_date":max_date,"max_price":max_price,"dep":dep, "origin1":origin1,"destination1":destination1})

def graph(request):
	import datetime
	origin = request.GET.get("origin")
	if origin is not None:
		destination = request.GET.get('destination')
		dep=request.GET.get('dep')
	else:
		origin = 'ICN'
		destination ='LHR'
		dep = '2017-06-04'
		print(origin)
		print(dep)
 	conn = sqlite3.connect("lapistadb.db")
	#DEP = datetime.date(2017, 6, 4)
	dep=datetime.date(int(dep[:4]),int(dep[5:7]),int(dep[8:10]))
	DEP=dep
 	TODAY = datetime.date.today()

	D1 = datetime.date.toordinal(DEP)
	D2 = (datetime.date.toordinal(TODAY))

  	dates = []
  	daysleft = []
  	for i in range(D2, D1):
		dates.append(str(datetime.date.fromordinal(i)))
 		daysleft.append(D1 - i)

 	cursor = conn.execute("SELECT ROUTE_ID from route where r_origin=(?) and r_dest=(?)",(origin,destination))
  	for row in cursor:
   	   route_i = str(row[0])
   	print(route_i)

  	scale_cost = []
  	for j in daysleft:
  	    cursor2 = conn.execute("SELECT COST from trend where ROUTE_ID=(?) and daysleft=(?)", (route_i, j))
  	    for row in cursor2:
 			scale_cost.append((float(row[0])))
 	print(scale_cost)
  	graph_cost = []
  	for i in range(len(scale_cost)):
 	    graph_cost.append(int(scale_cost[i] / scale_cost[0] * 100))
 	percent_cost=[i-100 for i in graph_cost]
  	axis = []
 	for i in range(len(scale_cost)):
  	    ax = {}
  	    ax["date"] = dates[i]
  	    ax["value"] = graph_cost[i]
  	    if graph_cost[i] is max(graph_cost):
  	    	ax["color"]="#CC0000"
  	    elif graph_cost[i] is min(graph_cost):
  	    	ax["color"]="#0054FF"
  	    ax["value2"]=round(percent_cost[i])
  	    axis.append(ax)
  	min_date=dates[graph_cost.index(min(graph_cost))]
  	max_date=dates[graph_cost.index(max(graph_cost))]
  	print(dates[graph_cost.index(min(graph_cost))])

  	print('axis',axis)
	return render(request, 'pages/graph.html',{"axis":axis,"min_date":min_date,"max_date":max_date})