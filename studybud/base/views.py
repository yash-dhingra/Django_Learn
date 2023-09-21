from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms=[x for x in range(0,100)]

def home(request):
    return render(request,'base/home.html',{'rooms':rooms})

def room(request):
    return render(request,'room.html')
