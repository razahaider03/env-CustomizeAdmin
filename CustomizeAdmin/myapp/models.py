from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.TextField(max_length=255)

    def __str__(self):
        return self.name