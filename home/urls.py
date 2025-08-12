from django.urls import path
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order_page, name='order_page'),
    path('reservation/', views.reservations,name='reservation'),
]