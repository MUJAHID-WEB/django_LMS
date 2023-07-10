from django.shortcuts import redirect, render

def BASE(request):
    return render(request, 'base.html')

def HOME(request):
    return render(request, 'main/home.html')