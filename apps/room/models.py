from django.db import models
from apps.hotel.models import Hotel

class Room(models.Model):

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    number = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    price_per_night = models.FloatField(blank=False, null=False)

    def __str__(self):
        return f'{self.hotel}'