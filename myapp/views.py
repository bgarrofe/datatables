from __future__ import unicode_literals

from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http import HttpResponse
from myapp.models import Person, Office, Vale
from myapp.tables import PersonTable
from django.core import serializers

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def people(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request, paginate={'per_page': 5}).configure(table)
    return render(request, 'people.html', {'table': table})
	
def example1(request):
    return render(request, 'example1.html', {})
	
def example2(request):
	person = Person.objects.all()
	dataSet = serializers.serialize('json', person)
	return render(request, 'example2.html', {'dataSet': dataSet})
	#return HttpResponse(json, content_type='application/json')

def example3(request):
    return render(request, 'example3.html', {})
	
def myModel_asJson(request):
	draw = request.GET.get('draw')
	columns = request.GET.getlist('columns')
	order = request.GET.get('order[0][dir]')
	start = int(request.GET.get('start'))
	length = int(request.GET.get('length'))
	
	#field = "id"
	
	if order == "asc":
		field = "id"
	else:
		field = "-id"
		
	end = start+length
	
	object_list = Vale.objects.all().order_by(field)[start:end]
	#object_list = Vale.objects.filter(pk=1) #or any kind of queryset
	json = serializers.serialize('json', object_list)
	return HttpResponse(json, content_type='application/json')