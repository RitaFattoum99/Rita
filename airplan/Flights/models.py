from django.db import models
from django.db.models.deletion import CASCADE
from django.shortcuts import render

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=64)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} {self.city}"


class Flight(models.Model):
    origin =  models.ForeignKey(Airport, on_delete=CASCADE, related_name="dipartured")
    destination = models.ForeignKey(Airport, on_delete=CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"from {self.origin} to {self.destination}"


class Passengers(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
