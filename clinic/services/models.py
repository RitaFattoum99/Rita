from django.db import models
import calendar
from calendar import HTMLCalendar

# Create your models here.


# class Doctor(models.Model):
#     f_nameD = models.CharField(max_length=64)
#     l_nameD = models.CharField(max_length=64)
#     birthD = models.DateField()
#     emailD = models.EmailField()
#     univercity = models.CharField(max_length=64)
#     experience = models.IntegerField()
#     time = models.TimeField()

#     def __str__(self):
#         return f"Name: {self.f_name} { self.l_name} Univercity: {self.univercity}"


class Patients(models.Model):
    f_name = models.CharField(max_length=64)
    l_name = models.CharField(max_length=64)
    birth = models.DateField()
    email = models.EmailField()
    symptoms = models.CharField(max_length=200)

    def __str__(self):
        return f"Name: {self.f_name} {self.l_name} Birth: {self.birth} Email: {self.email} Symptoms: {self.symptoms}"

# class Calendar(models.Model):
    