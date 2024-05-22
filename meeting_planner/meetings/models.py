from django.db import models
from datetime import date
from datetime import time
class Room(models.Model):
    name=models.CharField(max_length=(50))
    floorNumber= models.IntegerField()
    roomNumber= models.IntegerField()


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(1))
    duration = models.IntegerField(default=2)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)