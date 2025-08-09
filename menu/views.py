from django.shortcuts import render
ffrom .models import Menu

def homepage(request):
    query = request.GET.get('q', '')
    if query:
        items = Menu.objects.filter(name_icontainss=query)
        else:
            items = Menu.object.all()
            return render(request, 'homepage.html', {'items'items, 'query'})