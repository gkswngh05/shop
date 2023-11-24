from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'shopapp'

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("cart", views.cart, name="cart"),
    path("order", views.order, name="order"),
    path("register", views.register, name="register"),
    #path("account", views.account, name="account"),
    path("login", auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name="login"),
    path("logout", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
]