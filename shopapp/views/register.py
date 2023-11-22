from django.shortcuts import render
from django.shortcuts import redirect

def register(request):
    return render(request, 'register.html')