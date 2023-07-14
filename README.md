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

# Profile update page setup:
1. Template in 'registration/profile.html'

        -To show existing value by using 'value='{{user.first_name}}'' in input field

2. Url path in 'urls.py' 

            path('accounts/profile', user_auth.PROFILE, name='profile'),
            path('accounts/profile/update', user_auth.PROFILE_UPDATE, name='profile_update'),

3. functions in 'educamy/user_auth.py'

            def PROFILE(request):
                return render (request, 'registration/profile.html')

            def PROFILE_UPDATE(request):
             -- write functions --

4. Link in Account - {% url 'profile' %}

# Featured Courses Categories setup:
1. functions in 'app/models.py'

            class Categories(models.Model):
             -- write functions --

2. Register in 'app/admin.py'

        from .models import *

        admin.site.register(Categories)

3. Data fetch in 'educamy/views.py' by importing

        from app.models import Categories

        def HOME(request):
    
            category = Categories.objects.all().order_by('id')[0:5]
            -- and link to 'home.html'

4. cmd in terminal 

        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver

5. for icon: set link in 'base.html'

        <script src="https://kit.fontawesome.com/0c48ba20ec.js" crossorigin="anonymous"></script>

6. To show in Home page Featured Category Section

        {% for i in category %}       # category variable from 'views.py'

        <a class="btn-sm btn-pill me-1 mb-1 text-dark fw-medium px-6" 
            id="pills-art-tab" 
            data-bs-toggle="tab" 

            href="#pills-{{i.id}}" 

            role="tab" 
            aria-controls="pills-art" 
            aria-selected="false">
            
            {{i.name}}     # Categories name given in 'model.py'

        </a>

        {% endfor %}

# Courses setup:
1. functions in 'app/models.py' - Author, Courses
2. cmd in terminal 

        pip install pillow
        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver

3. Register in 'app/admin.py'
4. Data fetch in 'educamy/views.py' by importing

        from app.models import Categories

        def HOME(request):
    
            course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
            -- and link to 'home.html'

6. Show in Home page Featured Category Section
7. SHow media file - importing in 'urls.py'

        from django.conf import settings
        from django.conf.urls.static import static

        urlpatterns = [
            path('admin/', admin.site.urls),

        ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

8. To show discount price 

- functions in app/templatetags/course_tags.py

        from django import template
        import math
        register = template.Library()


        @register.simple_tag
        def discount_calculation(price, discount):
            if discount is None or discount is 0:
                return price
            sellprice = price
            sellprice = price - (price * discount/100)

            return math.floor(sellprice)

- fetch data in 'home.html'

        {% load course_tags %}

        <div class="col-auto px-2 text-right">
            <del class="font-size-sm">
                ${{i.price}}
            </del>
            <ins class="h4 mb-0 d-block mb-lg-n1">
                $ {%  discount_calculation i.price i.discount %}
            </ins>
        </div>


# Course List filter
1. Functions in models.py for category

        class Categories(models.Model):
        
        def get_all_category(self):
            return Categories.objects.all().order_by('id')

2. Functions in models.py for Level

        class Level(models.Model):
            name = models.CharField(max_length=100)


3. Register in admin.py for Level

        admin.site.register(Level)

4. cmd in terminal 

        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver


5. Functions in views.py for category, level and course get in course list

        def COURSE_LIST(request):
            category = Categories.get_all_category(Categories)
            level = Level.objects.all()
            course = Course.objects.all()
            context = {
                'category' : category,
                'level' : level,
                'course' : course,
            }
            return render(request, 'main/course_list.html', context)

6. fetch data in 'course_list.html'

# Course List filter wise course show
1. ajax cdn link in base.html

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

2. urls.py

        path('product/filter-data',views.filter_data,name="filter-data"),

3. Functions in views.py

        from django.template.loader import render_to_string
        from django.http import JsonResponse

        def filter_data(request):
            -- Functions --

4. fetch data in 'course_list.html'

        <script>
            $(document).ready(function(){
            
                $(".filter-checkbox").on('click', function(){
                    var filter_object={};
                    $(".filter-checkbox").each(function(index,ele){
                        var filter_value=$(this).val();
                        var filter_key=$(this).data('filter');
                        console.log(filter_key,filter_value);
                        filter_object[filter_key]=Array.from(document.querySelectorAll('input[data-filter='+filter_key+']:checked')).map(function(el){
                            return el.value;
                        });
                    });
            
                    $.ajax({
                        url:'{% url 'filter-data' %}',
                        data:filter_object,
                        dataType:'json',
                        success:function(res){
                            console.log(res)
                            $("#filteredCourses").html(res.data);
                            var filter_value=$(this).val();
                            var filter_key=$(this).data('filter');
                        }
                    });
                });
            });
        </script>

5. File in Templates/ajax/course.html - to show ajax result

# Search Option:

1. header.html - set search form

        <form class="w-100" method="get" action="{% url 'search'%}">
            <div class="input-group border rounded">
                <div class="input-group-prepend">
                    <button class="btn btn-sm text-secondary icon-xs d-flex align-items-center" type="submit">
                        <!-- Icon -->
                        
                    </button>
                </div>
                <input class="form-control form-control-sm border-0 ps-0" type="search" placeholder="What do you want to learn ?" aria-label="Search" name="query">
            </div>
        </form>


2. urls.py

        path('search', views.SEARCH, name="search"),

3. views.py 

        def SEARCH(request):
            -- functions -
            return render(request, 'search/search.html')

4. To show search result - templates/search/search.html

# Create Course Slug Automatically Using Title for Course Details page
1. models.py

        from django.utils.text import slugify
        from django.db.models.signals import pre_save

        class Course(models.Model):
            - functions -

            def get_absolute_url(self):
                from django.urls import reverse
                return reverse("course_details", kwargs={'slug': self.slug})


        def create_slug(instance, new_slug=None):
            - Functions -

2. urls.py

        path('course/<slug:slug>', views.COURSE_DETAILS, name="course_details"),

3. views.py

        def COURSE_DETAILS(request, slug):
            course = Course.objects.filter(slug = slug)
            if course.exists():
                course = course.first()
            else:
                return redirect('404')
            
            context = {
                'course': course
            }

            return render(request, 'course/course_details.html', context)

        def PAGE_NOT_FOUND(request):
            return render(request, 'error/404.html')

4. link in home.html to redirect to course details

        <a href="{{i.get_absolute_url}}"> </a>

5. if course not found redirect to 404 page

# What you learn and Requirements points set in Course overview
1. models.py

        # What_you_learn
        class What_you_learn(models.Model):
            course = models.ForeignKey(Course, on_delete=models.CASCADE)
            points = models.CharField(max_length=500)

            def __str__(self):
                return self.points

        # Requirements
        class Requirements(models.Model):
            course = models.ForeignKey(Course, on_delete=models.CASCADE)
            points = models.CharField(max_length=500)

            def __str__(self):
                return self.points

2. admin.py

        class What_you_learn_TabulaInline(admin.TabularInline):
            model = What_you_learn

        class Requirements_TabulaInline(admin.TabularInline):
            model = Requirements

        class course_admin(admin.ModelAdmin):
            inlines = (What_you_learn_TabulaInline, Requirements_TabulaInline)

        
        admin.site.register(Course, course_admin)
        admin.site.register(What_you_learn)
        admin.site.register(Requirements)

3. cmd in terminal 

        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver

4. course_details.html - overview tab

        <h3 class="mb-5">What you'll learn</h3>
        <div class="row row-cols-lg-2 mb-8">
            <div class="col-md">
                <ul class="list-style-v1 list-unstyled">
                    {% for learn in course.what_you_learn_set.all|slice:"0:5" %}
                    <li>{{learn.points}}</li>
                    {% endfor %}
                </ul>
            </div>

            <div class="col-md">
                <ul class="list-style-v1 list-unstyled ms-xl-6">

                    {% for learn in course.what_you_learn_set.all|slice:"5:10" %}
                    <li>{{learn.points}}</li>
                    {% endfor %}
                    
                </ul>
            </div>
        </div>

# Lesson part with video
1. models.py

        class Lesson(models.Model):
            -- Functions --
            
        class Video(models.Model):
            -- Functions --

2. Register in admin.py

        class Video_TabulaInline(admin.TabularInline):
            model = Video


        class course_admin(admin.ModelAdmin):
            inlines = (What_you_learn_TabulaInline, Requirements_TabulaInline, Video_TabulaInline)


        admin.site.register(Lesson)

3. cmd in terminal 

        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver
       
4. course_details.html - Curriculum tab

# Enroll 
1. Enroll button redirect to checkout page

        <a class="btn btn-primary btn-block mb-3" href="/checkout/{{course.slug}}">
            ENROLL
        </a>

2. urls.py
         
         path('checkout/<slug:slug>', views.CHECKOUT, name="checkout"),    

3. views.py 

        def COURSE_DETAILS(request, slug):
            course_id = Course.objects.get(slug = slug)
            try:
                enroll_status = UserCourse.objects.get(user= request.user, course= course_id)
            except UserCourse.DoesNotExist:
                enroll_status = None

            context = {
                'enroll_status' : enroll_status,
            }
            return render(request, 'course/course_details.html', context)
            

        def CHECKOUT(request, slug):
            -- functions --
            return render(request, 'checkout/checkout.html')

4. models.py

        from django.contrib.auth.models import User
         
        class UserCourse(models.Model):
            -- function --

5. cmd in terminal 

        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver

6. Register in admin.py

        admin.site.register(UserCourse)



