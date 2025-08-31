from .models import MenuItem

def menu_view(request):
    search_query = request.GET.get('search', '')
    if search_query:
        menu_items = MenuItem.objects.filter(name__icontains=search_query)
        else:
            menu_items = MenuItem.objects.all()
            return render(request, "menu.html", {"menu_items": menu_items,
            "search_query": search_query})
            
            return;