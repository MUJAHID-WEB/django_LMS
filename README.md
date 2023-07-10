# django_LMS

python3 -m venv eduenv

source eduenv/bin/activate

pip install django

django-admin startproject educamy .

# Now, Create apps
python3 manage.py startapp app

and add in educamy/settings.py

INSTALLED_APPS = [
  .......
    'app',
]

python3 manage.py migrate

python3 manage.py runserver

# Now, Create superuser
python3 manage.py createsuperuser

Username (leave blank to use 'mujahid'): mujahid
Email address: mujahid30390@gmail.com
Password: 12345678

# To save all pip in a file
pip3 freeze > requirements.txt

# Add 'static' & 'templates' folder
* static - css, js, images etc - put assets folder of templates


in settings.py

STATIC_URL = '/static/'

STATIC_ROOT= '/static/'

STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'static')
]

* templates - html files in different folders:
1. base.html - header & footer


in settings.py

TEMPLATES = [
    {
       .......

        'DIRS': ['templates'],

       .....
    },
]

# create 'views.py' file in educamy
and import in 'urls.py' for calling 'base' url

from .import views 

