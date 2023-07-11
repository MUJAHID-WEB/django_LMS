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

    # But for Auth, need to: 
        create 'user_auth.py' file in 'educamy'

        and user auth

            from django.contrib.auth.models import User
            from django.contrib import messages

            -- write authentication functions here --


        and import in 'urls.py' for calling 'base' url

            from .import views, user_auth
            urlpatterns = [
                path('accounts/register', user_auth.REGISTER, name='register'),
                path('dologin', user_auth.DO_LOGIN, name='dologin'),
            ]

    1. login.html

            <form class="mb-5" method='post' action='{% url 'dologin' %}'>
            {% csrf_token %}

            --give name in input field - name='email' --

            -- button type should be type="submit"
        
            </form>

    2. register.html 

                {% include 'components/msg.html'  %} # msg.html contains error, success and warning alert framework

                <form class="mb-5" method='post' action='{% url 'register' %}'>
                    {% csrf_token %}

                    --give name in input field - name='username' --

                    -- button type should be type="submit"
                
                </form>

    # To change Backend Login 'username' field to 'email' field:
    1. Create 'email_backend' file in 'app' folder
    2. import following to write functions 

            from django.contrib.auth import get_user_model
            from django.contrib.auth.backends import ModelBackend

            class EmailBackEnd(ModelBackend):
            def authenticate(self,  username=None, password=None, **kwargs):
            -- write functions --

    3. import following in 'user_auth.py' to write functions 

            from django.contrib.auth import authenticate,login,logout
            from app.email_backend import EmailBackEnd

            def DO_LOGIN(request):

            -- write functions --

    # Forget Password setup
    // smtp server settings in "settings.py"
        -------------------------------
        LOGIN_REDIRECT_URL = 'home'
        LOGOUT_REDIRECT_URL = 'login'


        EMAIL_USE_TLS = True
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_PORT = 587
        EMAIL_HOST_USER = 'Enter Email ID'
        EMAIL_HOST_PASSWORD = 'Enter Password'



        ---------------------------------------------
        Set url link in 'login.html'

            <a class="text-gray-800" href="{%url 'password_reset'%}">Forgot Password</a>



        // Create Html Templates
        -----------------------------------
        -templates
        -- registration
        ---- password_reset_form.html
        ---- password_reset_done.html
        ---- password_reset_confirm.html
        ---- password_reset_complete.html



        // install django-crispy-forms
        -------------

        pip install django-crispy-forms

        // settings
        -------------
        INSTALLED_APPS = [
            ......
            'crispy_forms',
        ]

        CRISPY_TEMPLATE_PACK = 'bootstrap4'



