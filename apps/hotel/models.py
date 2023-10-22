from django.db import models

class Hotel(models.Model):
    
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name}'