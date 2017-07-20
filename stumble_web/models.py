from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Place(models.Model):
    lat = models.DecimalField(decimal_places=6, max_digits=8)
    long = models.DecimalField(decimal_places=6, max_digits=9)
    name = models.TextField()


class Photos(models.Model):
    url = models.TextField()
    place = models.ForeignKey(Place)
    user = models.OneToOneField(User)
