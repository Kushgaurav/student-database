
from django.contrib import admin
from django.urls import path
from student import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("studentform", views.studentform, name="studentform"),
    path("view", views.view, name="view"),
    path("edit", views.edit, name="edit"),
    path("update", views.update, name="update"),
    path("delete", views.delete, name="delete")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
