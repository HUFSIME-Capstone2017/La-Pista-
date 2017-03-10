# -*- coding: utf-8 -*

from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate
# Create your views here.
def logo(request):
    candidates = Candidate.objects.all() 
    context = {'candidates':candidates}
    return render(request, 'logo/logo.html', context)
