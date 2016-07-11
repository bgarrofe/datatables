from __future__ import unicode_literals

from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http import HttpResponse
from myapp.models import Person, Office, Vale
from myapp.tables import PersonTable
from django.core import serializers
from django.db.models import Q
import json, operator

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
	
def Vale_asJson(request):
    draw = request.GET.get('draw')
    start = request.GET.get('start', default=0)
    length = request.GET.get('length', default=10)
    orderColIndex = request.GET.get('order[0][column]')
    field = request.GET.get('columns['+orderColIndex+'][data]')
    order = request.GET.get('order[0][dir]')
    value = request.GET.get('search[value]')
    
    if order == "desc":
        field = "-" + field
        
    end = int(start) + int(length)
	
    #get all rows
    query = Vale.objects.all()
    
    #count total rows
    filtered= total = query.count()
    
    #regex search
    fieldnames = ['name', 'job_id']
    
    
    if value != '':
        questions = [('name__contains', value), ('job_id__contains', value )]
        q_list = [Q(x) for x in questions]  
        qgroup = reduce(operator.or_, q_list)
        query = query.filter(qgroup)
        filtered = query.count()
    
    #get final fields
    query = query.order_by(field)[start:end]
    
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
    response_data['recordsFiltered'] = filtered
    response_data['data'] = data_objects
    
    return HttpResponse(json.dumps(response_data), content_type='application/json')