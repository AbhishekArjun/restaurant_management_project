from django.db import models

class Restaurant(models.Model):
    name = modelsCharField(max_length=255, verbose_name="Restaurant Name")
    address = models.TextField(verbose_name="Address", 
    
        def  _str_(self):
            return self.name
            
            