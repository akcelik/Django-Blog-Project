My Django Experiences
=========================
This aplication developed with Python (3.6) You can find required modules and versions below

## Requirements
* Django (3.0.3)
* django-ckeditor (5.9.0)
* django-cleanup (4.0.0)
* django-crispy-forms (1.8.1)
* django-js-asset (1.2.2)

## Database
Postgresql database is used in the project

"PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance."

Configuration
For the application to run smoothly, you should make the following configuration according to its environment.

settings.py
```
  ...
    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'databasename',
          'USER': 'username',
          'PASSWORD': 'password',
          'HOST': 'postgresqlhost',
          'PORT': '5432',
      }
  }
  ...
```

## Browsers
Please use Chrome browser to view the app properly
