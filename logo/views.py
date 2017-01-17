from django.shortcuts import render
from django.http	import HttpResponse

from .models	import Candidate
# Create your views here.
def logo(request):
	candidates = Candidate.objects.all() 
	context = {'candidates':candidates}
	return render(request, 'logo/logo.html', context)

def main(request):
    return render(request, 'logo/main.html')

def result(request):
    return render(request, 'logo/result.html')

def index(request):
    return render(request, 'logo/SRC/index.html')