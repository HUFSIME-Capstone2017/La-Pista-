# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http	import HttpResponse
from basic.forms import MainForm
import cplex
# Create your views here.
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

	LHR = "LHR"

	return render(request, 'pages/main.html',  {"adult_num": adult_num,
												"selected_value": selected_value,
												"kid_num": kid_num,
												"selected_value_kids": selected_value_kids,
												})

def result(request):
	adult_num=request.POST.get("adult_num")
	kid_num=request.POST.get("kid_num")
	depday=request.POST.get("depday")
	arrday=request.POST.get("arrday")
	LHR=request.POST.get("LHR")
	return render(request, 'pages/result.html', {"adult_num": adult_num,
												 "kid_num": kid_num,
												 "depday": depday,
												 "arrday": arrday,
												 "LHR": LHR,})

def list(request):
    return render(request, 'pages/list.html')

def detail(request):
    return render(request, 'pages/detail.html')

def warehouse(request):
    return render(request, 'pages/geo.html', {"caplbs": caplbs})

def logo(request):
	return render(request, 'pages/logo.html')
