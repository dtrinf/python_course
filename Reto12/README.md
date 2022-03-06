
# Reto 11


### Starting Postgres as a Docker container
```
docker run -d --rm \
    --name postgres \
    -e POSTGRES_USER=admin \
    -e POSTGRES_PASSWORD=changeme \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v $(pwd):/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres
```

### Conexion inside the contaiener
```
docker exec -it postgres bash
```

### Database and tables creation
```
psql -U admin -d admin

CREATE DATABASE reto11;

CREATE USER djangouser WITH ENCRYPTED PASSWORD 'djangopass';


ALTER ROLE djangouser SET client_encoding TO 'utf8';
ALTER ROLE djangouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE djangouser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE reto11 TO djangouser;
\q
```

### Conexion to new database
```
psql -U admin -d reto11
```

## Create Django project

django-admin startproject reto10


### Configure Django

```
cd reto11
vi reto11/settings.py

    DATABASES = {
        'default': {
            [...]
        }
    }
```

### Configure the database

```
python manage.py makemigrations 
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```


### Create new app

```
python manage.py startapp api_bookstore

vi reto11/settings.py

    INSTALLED_APPS = [
        [...]
        'api_bookstore',
        'rest_framework',
    ]

vi api_bookstore/models.py

python manage.py makemigrations

python manage.py migrate
```

# New model registration in admin

vi api_bookstore/admin.py

```
from .models import *

admin.site.register(api_author)
admin.site.register(api_book)
```

# We can see Hero model in admin interface

python manage.py runserver
http://127.0.0.1:8000/admin/


# New file to serialize database data with rest_framework

```
# vi api_bookstore/serializers.py
```

# Create Views to see serialized clases

```
# vi api_bookstore/views.py
```

# Add Authentication packages to be used

```
vi ./reto12/settings.py

    INSTALLED_APPS = [
        ...
        # Packages used to authenticate users and secure it
        'rest_framework.authtoken',
        'rest_auth',
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'rest_auth.registration',
    ]


    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    SITE_ID = 1
```
# Add URL's for RestAuth package

```
vi ./api_bookstore/urls.py



https://nextwebb.hashnode.dev/setup-social-authentication-in-django-rest-framework

https://github.com/iMerica/dj-rest-auth/blob/master/docs/installation.rst
