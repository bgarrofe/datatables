from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")
	
	
class Office(models.Model):
	name = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	office = models.CharField(max_length=100)
	age = models.IntegerField()
	start_date = models.DateField()
	salary = models.FloatField()
	
	def __unicode__(self):
		return self.name
		
class Vale(models.Model):
	job_id = models.CharField(max_length=20)
	start_date = models.DateField()
	birth_date = models.DateField()
	name = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
