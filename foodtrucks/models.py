from django.db import models


class FoodTruck(models.Model):
    locationid = models.IntegerField(primary_key=True)
    Applicant = models.TextField()
    Address = models.TextField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()
