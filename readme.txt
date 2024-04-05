2-K Dent Inventory Management System

base URL: https://2K-Dent.ims.cz/

- set up new project
    - create new project in pyCharm
    - install Django
        pip install Django
        pip install djangorestframework
    - start new Django project
        django-admin startproject database .
    - create new app
        django-admin startapp core
    - register new apps in settings.py
    ** don't make migrations before the model is created

- create accounts and superuser - knox auth
    - create accounts app
        django-admin startapp accounts
    - update settings.py
    - create User model
    - migrate changes to database
        python manage.py makemigrations
        python manage.py migrate
    - create superuser
        python manage.py createsuperuser
    - install django-rest-knox
        pip install django-rest-knox
    - create serializer for User
    - make migrations
    - create views for User
    - create urls for User

- connect with client-side (Angular)
    - install django cors header
        pip install django-cors-headers

- create Table model for sklady header
    - create Table model (Python class that represents a database table)
    - create Table serializer to convert complex data types (querysets, models,..) into native Python datatypes to be rendered into JSON, XML,.. for HTTP responses
    - create view for Table to render templates
    - add to urls
    - make migrations

- create TableHead model for sklady subheader
    - create TableHead model (Python class that represents a database table)
    - create TableHead serializer to convert complex data types (querysets, models,..) into native Python datatypes to be rendered into JSON, XML,.. for HTTP responses
    - create view for TableHead to render templates
    - add to urls
    - make migrations

- create Product model for sklady subheader
    - create Product model (Python class that represents a database table)
    - create Product serializer to convert complex data types (querysets, models,..) into native Python datatypes to be rendered into JSON, XML,.. for HTTP responses
    - create view for Product to render templates
    - add to urls
    - make migrations
    - add image to Product model
        - create form
        - create function in views to upload product image
        - install Pillow to provide support for manipulating file formats
            pip install pillow
        - add MEDIA roots to settings
        - add static() to urls to serve media files during development by mapping MEDIA_URL to the MEDIA_ROOT directory

- deploy to HEROKU
    - install python decouple to organize app settings so that can change the parameters without having to redeploy the app
        pip install python-decouple
    - create .env and store SECRET_KEY
    - instal dj-database-url to configure database settings from environment variables or URLs
        pip install dj-database-url
    - install dj-static to serve app with static files when deployed to production server
        pip install dj-static
    - freeze app requirements
        pip freeze > requirements-dev.txt
    - create requirements.txt
    - create Procfile specific for HEROKU
    - create runtime.txt
    - install heroku-config plugin to simplify the management of environment variables for Heroku apps through the Heroku CLI
        heroku plugins:install heroku-config
        - push all uncommitted changes to git
        - set up a Git remote named "heroku" for the Heroku app to enable deploying code directly to the Heroku app
            heroku git:remote -a ims-2kdent
        - push local env variables to Heroku app, ensuring consistency between development env and the deployed app
            heroku config:push
        - continue following the Deploy section in Heroku page
            * if error with SECRET_KEY:
            heroku config:set SECRET_KEY='app secret key'
            * if error with DEBUG:
            heroku config:set DEBUG=True
            - check heroku config
                heroku config
    - once the app is successfully uploaded to Heroku add the domain to ALLOWED_HOSTS in settings.py



