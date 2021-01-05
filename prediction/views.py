from django.shortcuts import render
from django.http import HttpResponse
from .models import Championdto
from django.core import serializers
# Create your views here.

def index(request) :
    rows = Championdto.objects.all()
    champions = serializers.serialize('json', rows)
    context = {'champions':champions}
    return render(request,'prediction/main.html',context)
