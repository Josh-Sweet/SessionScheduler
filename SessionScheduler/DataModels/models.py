from datetime import time
from django.db import models


class Location(models.Model):
    BuildingName = models.CharField(max_length=100)
    floor = models.IntegerField(default=1)
    roomNumber = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.BuildingName}\n Floor {self.floor}\n Room {self.roomNumber}"


class Session(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    startTime = models.TimeField(default=time(4))
    endTime = models.TimeField(default=time(5))
    Location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} from {self.startTime} to {self.endTime} on {self.date}"


class Attendant(models.Model):
    name = models.CharField(max_length=100)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} is attending {self.session}"