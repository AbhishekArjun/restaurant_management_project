from django.urls import path
from .view import menu_view

urlpatterns = [
    path('menu/', menu_view, name='menu'),
]