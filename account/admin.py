from django.contrib import admin

# Register your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def_str_(self):
        return self.name