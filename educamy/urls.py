
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base', views.BASE, name='base'),

    path('', views.HOME, name='home'),
    path('course_list', views.COURSE_LIST, name='course_list'),
    path('single_course', views.SINGLE_COURSE, name='single_course'),
]
