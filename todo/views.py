from django.shortcuts import render
from django.http import HttpResponse

def hello(requst) :
    return HttpResponse("Hello world!!")
    
# Create your views here.
