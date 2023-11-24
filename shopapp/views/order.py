from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def order(request):
    return HttpResponse("TODO")