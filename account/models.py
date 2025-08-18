from django.db import models

# Create your models here.
class Restaurant(model.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    def_str_(self):
        return self.name