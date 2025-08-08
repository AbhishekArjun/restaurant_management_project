from django.urls import path
from .view import menu_view

urlpatterns = [
    path(' ', views.homepage, name='homepage'),
]