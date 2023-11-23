from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from ..models import CartList

@login_required
def cart(request):
    # user = request.user
    # items = user.cartlist_set.filter().order_by()
    return render(request, 'cart.html')