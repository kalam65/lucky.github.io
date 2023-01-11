from django.db import models

# Create your models here.
class Employees(models.Model):
    Name=models.CharField(max_length=120)
    Email=models.CharField(max_length=140)
    Address=models.TextField(max_length=250)
    Phone=models.CharField(max_length=130)
    
    def __str__(self):
        return self.Name
    