from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Menu

def menu_view(request):
    items = MenuItem.object.all().order_by("name")
    paginator = Paginator(items, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "menu.html", {"page_obj": page_obj})