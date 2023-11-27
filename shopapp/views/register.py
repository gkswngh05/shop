from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from ..forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #return HttpResponse("Valid")
            form.save()
            return redirect("shopapp:index")
        render(request, 'register.html', {"form" : form})
    else: form = RegisterForm()
    return render(request, 'register.html', {"form" : form})