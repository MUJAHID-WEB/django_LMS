
from django.contrib import admin
from django.urls import path, include
from .import views, user_auth

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base', views.BASE, name='base'),
    path('404', views.PAGE_NOT_FOUND, name='404'),


    path('', views.HOME, name='home'),
    path('course_list', views.COURSE_LIST, name='course_list'),
    path('course/filter-data',views.filter_data,name="filter-data"),
    path('course/<slug:slug>', views.COURSE_DETAILS, name="course_details"),

    path('search', views.SEARCH, name="search"),
    
    path('about', views.ABOUT_US, name='about_us'),
    path('contact', views.CONTACT_US, name='contact_us'),

    path('accounts/', include(('django.contrib.auth.urls'))),
    path('accounts/register', user_auth.REGISTER, name='register'),
    path('dologin', user_auth.DO_LOGIN, name='dologin'),
    path('accounts/profile', user_auth.PROFILE, name='profile'),
    path('accounts/profile/update', user_auth.PROFILE_UPDATE, name='profile_update'),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
