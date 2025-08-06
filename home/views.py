from django.shortcuts import render

# Create your views here.
def contact_us(request):
    retrun render(request, "home/contact.html")