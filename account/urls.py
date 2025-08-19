from django.urls import path
from . import views

urlpatterns = [
    path("about-chef/", views.about_chef, name="about_chef"),
]
