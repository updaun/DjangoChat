from django.urls import path
from . import views

urlpatterns = [
    path("echo/", views.echo_page),
]