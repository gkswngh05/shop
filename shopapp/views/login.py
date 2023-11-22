from ..models import *
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("shopapp:index")
    
    if (not request.GET.get('userid') and not request.GET.get('password')) :
        return render(request, 'login.html')
    else:
        username = request.GET.get('userid')
        password = request.GET.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("shopapp:index")
        else:
            return redirect("shopapp:login")