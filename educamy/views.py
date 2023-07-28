from django.shortcuts import redirect, render
from app.models import *
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .settings import *
import razorpay
from time import time


client = razorpay.Client(auth=(KEY_ID, KEY_SECRECT))

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
    category = Categories.get_all_category(Categories)
    
    context = {
        'course': course,
        'category': category
    }
    return render(request, 'search/search.html', context)

# Course Details Page
def COURSE_DETAILS(request, slug):
    
    time_duration = Video.objects.filter(course__slug = slug).aggregate(sum = Sum('time_duration'))
    category = Categories.get_all_category(Categories)

    course_id = Course.objects.get(slug = slug)
    try:
        enroll_status = UserCourse.objects.get(user= request.user, course= course_id)
    except UserCourse.DoesNotExist:
        enroll_status = None

    course = Course.objects.filter(slug = slug)
    if course.exists():
        course = course.first()
    else:
        return redirect('404')
    
    context = {
        'course': course,
        'category' : category,
        'time_duration' : time_duration,
        'enroll_status' : enroll_status,
    }

    return render(request, 'course/course_details.html', context)

# 404 PAGE
def PAGE_NOT_FOUND(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category' : category,
    }
    return render(request, 'error/404.html', context)

# About Us page
def ABOUT_US(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category' : category,
    }
    return render(request, 'main/about_us.html', context)


# Contact Us page
def CONTACT_US(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category' : category,
    }
    return render(request, 'main/contact_us.html', context)

# Checkout

def CHECKOUT(request, slug):
    course = Course.objects.get(slug = slug)
    action = request.GET.get('action')
    order = None
    if course.price == 0:
        course = UserCourse(
            user = request.user,
            course = course
        )
        course.save()
        messages.success(request, 'You are enrolled in new course.')
        return redirect('my_course')
    
    elif action == 'create_payment':
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            country = request.POST.get('country')
            address_1 = request.POST.get('address_1')
            address_2 = request.POST.get('address_2')
            city = request.POST.get('city')
            state = request.POST.get('state')
            postcode = request.POST.get('postcode')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            comments = request.POST.get('comments')

            # amount = (course.price * 100)
            amount_cal = course.price - (course.price * course.discount / 100)
            amount = int(amount_cal) * 100

            currency = 'INR'
            notes = {
                'name': f'{first_name} {last_name}',
                'country' :country,
                'address': f'{address_1} {address_2}',
                'city' : city,
                'state' :state,
                'postcode' :postcode,
                'phone' :phone,
                'email' :email,
                'comments' :comments,
            }
            receipt = f' educamy-{int(time())}'
            order = client.order.create(
                {
                    'receipt' :receipt,
                    'notes' :notes,
                    'amount' :amount,
                    'currency' :currency,
                }
            )

            payment = Payment(
                course = course,
                user = request.user,
                order_id = order.get('id')
            )
            payment.save()


    context = {
        'course': course,
        'order' : order,
        
    }    
    return render(request, 'checkout/checkout.html', context)

# Verify Payment
@csrf_exempt
def VERIFY_PAYMENT(request):
    if request.method == 'POST':
        data = request.POST
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_order_id']

            payment = Payment.objects.get(order_id = razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True

            usercourse = UserCourse(
                user = payment.user,
                course = payment.course
            )
            usercourse.save()
            payment.user_course = usercourse
            payment.save()

            context = {
                'data': data,
                'payment': payment
                
            }
            return render(request, 'verify_payment/success.html', context)
        except:
            return render(request, 'verify_payment/fail.html')


# My Crouse
def MY_COURSE (request):
    course = UserCourse.objects.filter(user = request.user)

    context = {
        'course': course,
        
    }
    return render(request, 'course/my_course.html', context)

# WAtch Course

def WATCH_COURSE (request, slug):
    course = Course.objects.filter(slug = slug)
    lecture = request.GET.get('lecture')
 
    video = Video.objects.filter(id = lecture)


    if course.exists():
        course = course.first()
    else:
        return redirect('404')
        
    context = {
        'course' : course,
        'video' : video,
   
    }
    return render(request, 'course/watch_course.html', context)