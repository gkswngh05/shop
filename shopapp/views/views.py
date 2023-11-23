from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from ..models import *
from django.contrib.auth import authenticate, logout, login

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def join(request):
    if request.user.is_authenticated:
        return redirect("shopapp:index")
    if request.GET.get('join') != '1':
        return render(request, 'join.html')
    dict = request.GET.copy()

    try :
        myUser.objects.create(
            userId = dict['userId'],
            name = dict['name'],
            password = dict['password'],
            callNumber = dict['callNumber'],
            role = int(dict['role']),
            address = dict['address'],
        )
        return HttpResponse("계정 생성 완료")
    except:
        return HttpResponse("계정 생성 오류")

@login_required
def view(request):
    id = request.GET.get('id')
    if id == None: return HttpResponse("No id")
    try:
        item = Item.objects.get(id = id)
    except:
        return HttpResponse("Invalid id")
    #return HttpResponse(item.objects)
    return render(request, 'view.html', {"item" : item})
    


@login_required
def account(request):
    userId = request.GET.get('user')
    try:
        user = myUser.objects.get(id = userId)
    except:
        return HttpResponse("Invalid user")
    return render(request, 'account.html', {"user" : user})