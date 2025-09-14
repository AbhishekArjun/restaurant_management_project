from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):
        from . import __init__ as constants
        from .models import OrderStatus

        try:
            for status in constants.DEFAULT_STATUSES:
                OrderStatus.objects.get_or_create(name=status)
                except OperationalError:
                    pass
