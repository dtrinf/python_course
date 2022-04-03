
# Final Project


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

CREATE DATABASE web_lfg_new;

CREATE USER djangouser WITH ENCRYPTED PASSWORD 'djangopass';


ALTER ROLE djangouser SET client_encoding TO 'utf8';
ALTER ROLE djangouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE djangouser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE web_lfg TO djangouser;
\q
```

### Conexion to new database
```
psql -U admin -d web_lfg
```

## Create Django project

django-admin startproject web_lfg


### Configure Django

```
cd web_lfg
vi web_lfg/settings.py

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
python manage.py startapp api

vi reto11/settings.py

    INSTALLED_APPS = [
        [...]
        'api',
        'rest_framework',
    ]

vi api/models.py
```


# Create new CustomUser model

vi api/models.py

```
class CustomUser
   pass
```

vi settings.py

```
AUTH_USER_MODEL = 'api.CustomUser'
```


python manage.py makemigrations

python manage.py migrate

# Create new form to create/modify user

vi api/forms.py


# Register new forms

vi api/admin.py

```

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
vi ./web_lfg/settings.py

    INSTALLED_APPS = [
        ...
        ### Reto12
        # Packages used to authenticate users and secure it
        'rest_framework.authtoken',
        # Package for log in, log out, and password reset API endpoints
        'dj_rest_auth',
        # # django-allauth package to enable a standard registration process
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'dj_rest_auth.registration',
    ]


    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    SITE_ID = 1
```
# Add URL's for RestAuth package to allow Rest Authentication

```
vi ./api_bookstore/urls.py

urlpatterns = [
    ...
    # URL's for dj_rest_auth package
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')), #
]
```




https://nextwebb.hashnode.dev/setup-social-authentication-in-django-rest-framework

https://github.com/iMerica/dj-rest-auth/blob/master/docs/installation.rst

https://kaurlearning.com/wp-content/uploads/2021/03/Django-for-APIs.pdf