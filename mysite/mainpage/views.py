from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index2(request):
	return render(request, 'mainpage/index.html')