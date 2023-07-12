from django.shortcuts import redirect, render
from app.models import Categories



# Base part
def BASE(request):
    return render(request, 'base.html')

# Home Page
def HOME(request):
    
    category = Categories.objects.all
    context = {
        'category' : category,
    }

    return render(request, 'main/home.html', context)

# Cours list page
def COURSE_LIST(request):
    return render(request, 'main/course_list.html')


# Course Details Page
def SINGLE_COURSE(request):
    return render(request, 'main/single_course.html')


# About Us page
def ABOUT_US(request):
    return render(request, 'main/about_us.html')


# Contact Us page
def CONTACT_US(request):
    return render(request, 'main/contact_us.html')

