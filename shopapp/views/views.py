from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpRequest
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
        User.objects.create(
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
def cart(request):
    return HttpResponse("TODO")
    # tmp = ""
    # userId = request.GET.get('user')
    # itemId = request.GET.get('itemId')
    # try:
    #     itemAmount = int(request.GET.get('itemAmount'))
    # except:
    #     itemAmount = None
    
    # try:
    #     user = User.objects.get(id = userId)
    # except:
    #     return HttpResponse("Invalid user")
    
    # if itemId != None:
    #     if itemAmount == None: return HttpResponse("Invalid Amount")
    #     try:
    #         item = Item.objects.get(id = itemId)
    #     except:
    #         return HttpResponse("Invalid id")
    #     user.cartItems.remove(item)
    #     Cart.objects.create(customer = user, item = item, amount = itemAmount)
    #     tmp += "장바구니 담기 성공\n"

    # #return HttpResponse(user).cart_set.all())
    # tmp += f"{user.username}의 장바구니\n"
    # for i in user.cart_set.all():
    #     tmp += f"이름: {i.item.name} 갯수: {i.amount}, 단가: {i.item.price} 원\n"
    # return HttpResponse(tmp)
    #return render(request, 'view.html', {"item" : item, "seller_Name" : 0})


@login_required
def account(request):
    userId = request.GET.get('user')
    try:
        user = User.objects.get(id = userId)
    except:
        return HttpResponse("Invalid user")
    return render(request, 'account.html', {"user" : user})