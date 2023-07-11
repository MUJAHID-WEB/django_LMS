from django.shortcuts import redirect, render

def BASE(request):
    return render(request, 'base.html')

def HOME(request):
    return render(request, 'main/home.html')

def COURSE_LIST(request):
    return render(request, 'main/course_list.html')

def SINGLE_COURSE(request):
    return render(request, 'main/single_course.html')

def ABOUT_US(request):
    return render(request, 'main/about_us.html')

def CONTACT_US(request):
    return render(request, 'main/contact_us.html')

