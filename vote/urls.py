from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns

urlpatterns = patterns('vote.views',
	url(r'^choix$', 'choix'),
)