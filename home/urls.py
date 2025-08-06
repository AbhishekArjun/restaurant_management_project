from django.urls import path
from .views import *

urlpatterns = [
    path('reservation/', views.reservations,name='reservation'),
]