from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('Hello Django')

def index1(request):
    return HttpResponse('Hey this is second page')

def index2(request):
    return render(request,'App1_index.html')