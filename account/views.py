from django.shortcuts import render
from .models import Restaurant
# Create your views here.
def home(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'homepage.html', { 'restaurant':restaurant})
    