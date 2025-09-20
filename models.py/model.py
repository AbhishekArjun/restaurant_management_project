from django.sb import models
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TestField()
    price = models.DeciamlField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    is_available = models.models.BooleanField(default=True)
    def _str_(self):
        return self