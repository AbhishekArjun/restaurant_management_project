from django.contrib import admin
from .models import Menu, Order
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
list_display = ('name','price','description','available')
search_fields = ('name',)
list_filter = ('available',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','menu_item','quantity','ordered_at')
    search_fields = ('user_username','menu_item_name')
    list_filter = ('ordered_at')