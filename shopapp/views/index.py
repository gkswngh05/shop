from django.shortcuts import render
from django.shortcuts import redirect

from ..models import Item

def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {"items" : items})