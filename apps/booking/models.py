from django.db import models
from apps.room.models import Room
from apps.guest.models import Guest

class Booking(models.Model):

    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, blank=True, null=True)
    check_in_date = models.DateField(auto_now=True)
    check_out_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.room}'