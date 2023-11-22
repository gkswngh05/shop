from django.urls import path

from . import views

app_name = 'shopapp'

urlpatterns = [
    path("", views.index, name="index"),
    path("view", views.view, name="view"),
    path("cart", views.cart, name="cart"),
    path("join", views.join, name="join"),
    path("account", views.account, name="account"),
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutPage, name="logout"),
]