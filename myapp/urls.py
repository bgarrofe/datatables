from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.people, name='people'),
	url(r'^example1/$', views.example1, name='example1'),
	url(r'^example2/$', views.example2, name='example2'),
	url(r'^example3/$', views.example3, name='example3'),
	url(r'^vale_ajax_url$', views.Vale_asJson, name='vale_ajax_url'),
]