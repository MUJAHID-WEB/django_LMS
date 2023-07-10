from django.shortcuts import redirect, render

def BASE(request):
    return render(request, 'base.html')