from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns

urlpatterns = [
    url(r'^vote/', include('vote.urls')),
	url(r'^presentation/', include('presentation.urls'))
]
