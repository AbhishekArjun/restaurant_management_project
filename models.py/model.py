from django.sb import models
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    def _str_(self):
        return self.name