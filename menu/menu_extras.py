from django import template

register = template.Library()

@register.filter
def coming_soon(is_available):
   """
   If the menu item is not available , return 'Coming Soon',
   otherwise return an empty string.
   """
   return "" if is_available else "Coming Soon" 
