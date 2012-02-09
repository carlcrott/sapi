from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf.urls.defaults import *
from seq_api.api import GeneResource
admin.autodiscover()

gene_resource = GeneResource()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(gene_resource.urls)),
)
