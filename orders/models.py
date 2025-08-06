from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    email = models.EmailField()
    enrolled_date = models.DataField(auto_now_add=True)
    def_str_(self):
        return self.name