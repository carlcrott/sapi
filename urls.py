from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf.urls.defaults import *
from tastypie.api import Api
from seq_api.api import GeneResource, UserResource
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(GeneResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
