
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







