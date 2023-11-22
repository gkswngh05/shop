from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'shopapp'

urlpatterns = [
    path("", views.index, name="index"),
    path("view", views.view, name="view"),
    path("cart", views.cart, name="cart"),
    path("register", views.register, name="register"),
    path("account", views.account, name="account"),
    path("login", auth_views.LoginView.as_view(template_name="login.html", next_page="/", redirect_authenticated_user=True), name="login"),
    path("logout", auth_views.LogoutView.as_view(template_name="logout.html", next_page="/"), name="logout"),
]