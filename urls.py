from django.urls import path
from . import views

urlpatterns = [
    path('menu/', viewss.menu_item_list, namr='menu'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]