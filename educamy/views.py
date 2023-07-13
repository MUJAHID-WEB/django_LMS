from django.shortcuts import redirect, render
from app.models import *
from django.template.loader import render_to_string
from django.http import JsonResponse



# Base part
def BASE(request):
    return render(request, 'base.html')

# Home Page
def HOME(request):

    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
    context = {
        'category' : category,
        'course' : course,
    }

    return render(request, 'main/home.html', context)

# Cours list page
def COURSE_LIST(request):
    category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    free_course_count = Course.objects.filter(price = 0).count()
    paid_course_count = Course.objects.filter(price__gte = 1).count()

    context = {
        'category' : category,
        'level' : level,
        'course' : course,
        'free_course_count' : free_course_count,
        'paid_course_count' : paid_course_count,
    }
    return render(request, 'main/course_list.html', context)

# filtered course 
def filter_data(request):
    categories = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')
    #print(price)


    if price == ['pricefree']:
       course = Course.objects.filter(price=0)
    elif price == ['pricepaid']:
       course = Course.objects.filter(price__gte=1)
    elif price == ['priceall']:
       course = Course.objects.all()

    elif categories:
       course = Course.objects.filter(category__id__in=categories).order_by('-id')
    elif level:
       course = Course.objects.filter(level__id__in = level).order_by('-id')
    else:
       course = Course.objects.all().order_by('-id')

    context = {
        'course': course
    }


    t = render_to_string('ajax/course.html', context)

    return JsonResponse({'data': t})


# Search
def SEARCH(request):
    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)
    context = {
        'course': course
    }
    return render(request, 'search/search.html', context)

# Course Details Page
def SINGLE_COURSE(request):
    return render(request, 'main/single_course.html')


# About Us page
def ABOUT_US(request):
    return render(request, 'main/about_us.html')


# Contact Us page
def CONTACT_US(request):
    return render(request, 'main/contact_us.html')

