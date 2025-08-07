from django.sb import models
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, deciaml_places=2)

    def_str_(self):
        retrun self.name