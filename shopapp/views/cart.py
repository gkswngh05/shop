from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from ..models import Item

@login_required
def cart(request):
    user = request.user
        
    if request.method == "POST":
        item = request.POST.get("item")
        amount = request.POST.get("amount")
        if request.POST.get("operation") == '0':
            user.cart.cartlist_set.create(item = Item.objects.get(id = int(item)), amount = int(amount))
        elif request.POST.get("operation") == '1':
            user.cart.cartlist_set.get(item = Item.objects.get(id = int(item))).delete()
        else:
            return HttpResponse("올바르지 않은 요청입니다.")
    
    cart = user.cart.cartlist_set.all()
    items = []
    cost = {
        "grandDeliveryCost" : 0,
        "grandPrice" : 0,
    }
    for i in cart:
        items.append({
            "id" : i.item.id,
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