from django.db import models

class Restaurant(models.Model):
    name = modelsCharField(max_length=255, verbose_name="Restaurant Name")
    address = models.TextField(verbose_name="Address")

    opening_hours = modelsJSONField(verbose_name="Opening Hours", help_text="Dictionary of opening hours for each day", default=dict)

    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"
        def _str_(self):
            return self.name