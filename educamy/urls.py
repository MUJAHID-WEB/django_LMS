
from django.contrib import admin
from django.urls import path, include
from .import views, user_auth

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base', views.BASE, name='base'),

    path('', views.HOME, name='home'),
    path('course_list', views.COURSE_LIST, name='course_list'),
    path('single_course', views.SINGLE_COURSE, name='single_course'),
    path('about', views.ABOUT_US, name='about_us'),
    path('contact', views.CONTACT_US, name='contact_us'),

    path('accounts/', include(('django.contrib.auth.urls'))),
    path('accounts/register', user_auth.REGISTER, name='register'),
    path('dologin', user_auth.DO_LOGIN, name='dologin'),
]
