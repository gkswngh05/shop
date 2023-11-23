from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from ..models import *

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def about(request):
    return render(request, 'about.html')