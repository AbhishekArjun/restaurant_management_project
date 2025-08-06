from django.shortcuts import render

# Create your views here.
from .model import Restaurant

def home_view(request):
    restaurant = Restaurant.objects.first()
    context = {
        'restaurant_name': restaurant.name if restaurant else 'Restaurant',
        'restaurant_phone': restaurant.phone if restaurant else 'N/A'

    }
    return render(request, 'home.html', context)
