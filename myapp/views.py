from __future__ import unicode_literals

from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http import HttpResponse
from myapp.models import Person, Office, Vale
from myapp.tables import PersonTable
from django.core import serializers
import json

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
    start = request.GET.get('start', default=0)
    length = request.GET.get('length', default=5)
    
    field = "id"
    
    if order == "asc":
        field = "id"
    else:
        field = "-id"
        
    end = 0
    end = int(start) + int(length)
	
    total = Vale.objects.count()
    query = Vale.objects.order_by(field)[start:end]
    
    
    data_objects = []
    for q in query:
        result = {}
        result['job_id'] = q.job_id
        result['start_date'] = q.start_date.isoformat()
        result['birth_date'] = q.birth_date.isoformat()
        result['name'] = q.name
        result['department'] = q.department
        result['position'] = q.position
        result['email'] = q.email
        data_objects.append(result)
    
    response_data = {}
    response_data['draw'] = draw
    response_data['recordsTotal'] = total
    response_data['recordsFiltered'] = total
    response_data['data'] = data_objects
    
    return HttpResponse(json.dumps(response_data), content_type='application/json')