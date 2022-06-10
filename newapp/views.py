from django.http import HttpResponse
from django.template import loader
from .models import newapp
from .models import daneshjo
from .models import info_dars
from django.shortcuts import render,redirect

def index(request):
	return render(request,'index.html')



def daneshjo1(request):
       mydaneshjo = daneshjo.objects.all().values()
       template = loader.get_template('sidebar-left.html')
       context = {
               'mydaneshjo': mydaneshjo,
              }
       return HttpResponse(template.render(context, request))    


def vahed(request):
       mymembers = newapp.objects.all().values()
       template = loader.get_template('sidebar-right.html')
       context = {
              'mymembers': mymembers,
       }
       return HttpResponse(template.render(context, request))

def info_dars1(request):
  mydars = info_dars.objects.all().values()
  template = loader.get_template('basic-grid.html')
  context = {
    'mydars': mydars,
  }
  return HttpResponse(template.render(context, request))


'''def index(request):

#return render(request, 'index.html')
  mymembers = newapp.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))'''




'''def info_dars1(request):
  mydars = info_dars.objects.all().values()
  template = loader.get_template('info_dars.html')
  context = {
    'mydars': mydars,
  }
  return HttpResponse(template.render(context, request))'''
