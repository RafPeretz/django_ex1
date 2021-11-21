from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import json

# Create your views here.
def homepage(request):
    return HttpResponse('hello')

def about (request):
    return HttpResponse('about.html')

def today(request):
    return HttpResponse(str(datetime.today()))

def homepage(request):
    with open('data.json') as f:
        data = json.load(f)
        hello = 1
    return render(request, 'homepage.html', context={'people': data})

