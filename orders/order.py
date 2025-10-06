from django.db import models
class OderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__in=['pending', 'processing'])

        class Order(models.Model):
            status = models.CharField(max_length=20, choices=[
                ('pending', 'Pending'),
            ]

            status = models.CharField(max_length=20, choices=)