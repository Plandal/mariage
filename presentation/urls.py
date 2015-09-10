from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns

urlpatterns = patterns('presentation.views',
	url(r'^accueil$', 'accueil'),
	url(r'^maries$', 'maries'),
	url(r'^temoins$', 'temoins'),
	url(r'^lieu$', 'lieu'),
	url(r'^photos$', 'photos'),
	url(r'^contact$', 'contact'),
)