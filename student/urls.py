
from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path("",views.index, name="index"),
    path("login",views.login, name="login")

]