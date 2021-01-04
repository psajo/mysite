from django.shortcuts import render
from django.http import HttpResponse
from .models import Championdto
# Create your views here.

def index(request) :
    champions = Championdto.objects.all()
    context = {'champions':champions}
    return render(request,'prediction/main.html',context)
