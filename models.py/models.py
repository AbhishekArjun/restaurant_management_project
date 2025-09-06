from django.db import models

class Restaurant(models.Model):
    name = modelsCharField(max_length=255, verbose_name="Restaurant Name")
    address = models.TextField(verbose_name="Address", 
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blnk=True, null=True)
    
        def  __str__(self):
            return self.name
            
            