
# dabase is sick/sickness
# thrive is the main account in django


"""
Directions taken from
http://django-tastypie.readthedocs.org/en/latest/tutorial.html
"""

"""
Latest working URLs:
http://127.0.0.1:8000/api/v1/user/schema/?format=json
http://127.0.0.1:8000/api/v1/user/set/1;3/?format=json
http://127.0.0.1:8000/api/v1/entry/schema/?format=json
http://127.0.0.1:8000/api/v1/entry/1/?format=json
"""

### Process

## Project setup
$ django-admin.py startproject sapi
$ cd sapi/

# verify project integrity
$ python manage.py runserver

# ----------------- should see something like -------------------- #
0 errors found
Django version 1.3.1, using settings 'sapi.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
# ---------------------------------------------------------------- #

# kill it with CONTROL-C


## Database

# Server side setup
#  - create system user ( if need be )

# setup of database http://www.cyberciti.biz/faq/howto-add-postgresql-user-account/
#  - create database owner
#  - create database
#  - grant owner privs


$ python manage.py syncdb

# create django project super user

# Enable admin
# ----------------------- within sapi/settins.py ----------------------- #
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)
# ---------------------------------------------------------------------- #

# Enable the URLS to admin
# ----------------------- within sapi/urls.py -------------------------- #
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
# ---------------------------------------------------------------------- #

# open http://127.0.0.1:8000/admin/ in browser

# should see "Django administration"


## API setup

$ python manage.py startapp seq_api
$ cd seq_api

# paste tastypie in seq_api file

# ----------------------- within sapi/seq_api/models.py -------------------------- #
from tastypie.utils import now
from django.contrib.auth.models import User
from django.db import models # this was the only default in this file
from django.template.defaultfilters import slugify

class Gene(models.Model):
  user = models.ForeignKey(User)
#  pub_date = models.DateTimeField(default=now)
  name = models.CharField(max_length=100)
  sequence = models.CharField(max_length=100000)
  chromosome = models.CharField(max_length=10)
  slug = models.SlugField()

  def __unicode__(self):
    return self.title

  def save(self, *args, **kwargs):
    # For automatic slug generation.
    if not self.slug:
      self.slug = slugify(self.title)[:50]

    return super(Entry, self).save(*args, **kwargs)
# -------------------------------------------------------------------------------- #


# install tastypie requirements
# http://django-tastypie.readthedocs.org/en/latest/tutorial.html#installation


# Enable tastypie
# ------------------------- within sapi/settins.py ------------------------- #
INSTALLED_APPS = (
    ...
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'tastypie',
)
# -------------------------------------------------------------------------- #


# Create the Gene resources
# ----------------------- within sapi/seq_api/api.py ----------------------- #
from tastypie.resources import ModelResource
from seq_api.models import Gene

class GeneResource(ModelResource):
  class Meta:
    queryset = Gene.objects.all()
    resource_name = 'gene'
# -------------------------------------------------------------------------- #


# Creating URLs for resource access
# ----------------------- replace sapi/urls.py ------------------------- #
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
# ---------------------------------------------------------------------- #

# verify that the login / admin still work
http://127.0.0.1:8000/admin/

# Check out some of the resources!
http://127.0.0.1:8000/api/gene/?format=json
http://127.0.0.1:8000/api/gene/schema/?format=json

# Make an API call 
$ curl -H "Accept: application/json" http://127.0.0.1:8000/api/gene/?format=json


# Connect the users for authenticaion
# ----------------------- within sapi/seq_api/api.py ----------------------- #
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from seq_api.models import Gene

class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'user'

class GeneResource(ModelResource):
  user = fields.ForeignKey(UserResource, 'user')
  class Meta:
    queryset = Gene.objects.all()
    resource_name = 'gene'
# ---------------------------------------------------------------------- #


# Expand the API w versioning and links to necessary user resources
# ----------------------- replace sapi/urls.py ------------------------- #
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
# ---------------------------------------------------------------------- #


# Restrict fields and methods
# ----------------------- add within sapi/seq_api/api.py ----------------------- #
class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'user'
    excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
    allowed_methods = ['get']
# ------------------------------------------------------------------------------ #















