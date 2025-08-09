from django.shortcuts import render
from .models import Restaurant
# Create your views here.
def home(request):
   cart = request.session.get('cart', [])
   cart_count = len(cart)
   return render(request, 'home.html', {'cart_count' : cart_count})
   