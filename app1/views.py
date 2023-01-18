from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def  third(request):
    return render(request,'third.html')


def four(request):
    return HttpResponse('<h1>this is my fourth file</h1>')