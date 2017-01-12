# -*- coding: utf-8 -*

from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate
# Create your views here.
def index(request):
    candidates = Candidate.objects.all() 
    context = {'candidates':candidates}
    return render(request, 'elections/Index.html', context)

def temp(request):
    return render(request, 'elections/templates3.html')
