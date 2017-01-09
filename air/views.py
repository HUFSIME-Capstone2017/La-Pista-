from django.shortcuts import render
from django.http	import HttpResponse

from .models	import Candidate
# Create your views here.
def index(request):
	candidates = Candidate.objects.all() 
	context = {'candidates':candidates}
	return render(request, 'air/index.html', context)

def main(request):
    return render(request, 'air/main.html')