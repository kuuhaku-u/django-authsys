from re import template
from turtle import home
from django.urls import path
from .import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',views.home),
    path('register/',views.register),
    path('profile/',views.profile),
    path('login/',auth_view.LoginView.as_view(template_name = 'users/login.html'),name = 'log_in'),
    path('logout/',auth_view.LogoutView.as_view(template_name = 'users/logout.html'),name = 'log_out'),
]
