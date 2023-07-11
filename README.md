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

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]

* templates - html files in different folders:
1. base.html - to load static and connect with header, footer and others - 

        <head>
            {% load static %}

    and link with static like below: 

        <link rel="stylesheet" href="{% static 'assets/fonts/fontawesome/fontawesome.css' %}">

        <img src="{% static 'assets/img/brand-dark.svg' %}" class="navbar-brand-img" alt="...">

        </head>
        <body>

            {% include 'components/header.html' %}

        </body>

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

2. main/home.html - 

   -- to show home page set url in 'urls.py' and functions in 'views.py'

   -- extend base files in home.html

        {% extends 'base.html' %}
        {% load static %}

        {% block content %} 
        
        --paste the design --

        {% endblock %}

    -- And in base file between header and footer

        {% block content %} 
        
        {% endblock %}

3. main/course_list.html - 

   -- to show course_list page set url in 'urls.py' and functions in 'views.py'

   -- extend base files in 'course_list.html'

        {% extends 'base.html' %}
        {% load static %}

        {% block content %} 

        --paste the design --
        
        {% endblock %}
        
4. main/single_course.html
5. main/contact_us.html
6. main/about_us.html

7. registration - set authentic url in 'urls.py' 

        from django.urls import path, include
        
        urlpatterns = [
            path('accounts/', include(('django.contrib.auth.urls'))),
        ]

    This function gives the created url ' ../accounts/login'

    1. login.html

    # But for register, need to: 
    create 'user_auth.py' file in 'educamy'

    and import in 'urls.py' for calling 'base' url

        from .import views, user_auth
        urlpatterns = [
        path('accounts/register', user_auth.REGISTER, name='register'),
        ]

    2. register.html

