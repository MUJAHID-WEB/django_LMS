from django.shortcuts import redirect, render

def REGISTER(request):
    return render(request, 'registration/register.html')