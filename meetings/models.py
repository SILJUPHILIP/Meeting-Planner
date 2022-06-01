import datetime
from pyexpat import model
from django.db import models
from datetime import datetime


# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length= 25)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"The meeting is conducting at {self.room_name} on room {self.room_number}, {self.floor_number} floor"

class Meetings(models.Model):
    meeting_name = models.CharField(max_length = 255)
    created_time = models.DateTimeField(default = datetime.now())
    start_time = models.DateTimeField()
    duration = models.FloatField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.meeting_name} starts at {self.start_time} and duration of {self.duration} hour(s)"
