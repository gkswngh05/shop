from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from ..models import CartList

@login_required
def cart(request):
    user = request.user
    cart = user.cart.cartlist_set.all()
    items = []
    cost = {
        "grandDeliveryCost" : 0,
        "grandPrice" : 0,
    }
    for i in cart:
        items.append({
            "name" : i.item.name,
            "amount" : i.amount,
            "seller" : i.item.sellerid.name,
            "deliveryCost" : i.item.deliveryCost,
            "price" : i.item.price,
            "totalPrice" : i.item.price * i.amount,
            })
        cost["grandDeliveryCost"] += i.item.deliveryCost
        cost["grandPrice"] += i.item.price * i.amount
    
    print(items)
    return render(request, 'cart.html', {"items" : items, "cost" : cost})