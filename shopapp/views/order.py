from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from ..forms import OrderForm



@login_required
def order(request):
    user = request.user
    # if request.method == "POST":
    #     return HttpResponse("TODO")
    
    cart = user.cart.cartlist_set.all()

    if request.method == 'POST':
        formdic = request.POST.copy()
        formdic["customer"] = user
        for i in cart:
            formdic["itemCode"] = i.item
            formdic["amount"] = i.amount
            form = OrderForm(formdic)
            if form.is_valid():
                form.save()
            cart.delete()
        return redirect("shopapp:index")
    
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

    form = OrderForm(initial={"receiverName" : request.user.userName, "receiverNumber" : request.user.callNumber, "receiverAddress" : request.user.address})
    return render(request, 'order.html', {"form" : form, "items" : items, "cost" : cost})