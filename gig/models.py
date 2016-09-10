from __future__ import unicode_literals

from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Create your models here.
class Gig(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    lon = models.FloatField()
    lat = models.FloatField()
    provider = models.ForeignKey(AUTH_USER_MODEL)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    expires = models.DateField()
    category = models.ForeignKey('Category')
    pictureurl = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    postnumber = models.IntegerField()
    city = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Transaction(models.Model):
    offer = models.ForeignKey('Offer')
    time = models.TimeField()
    date = models.DateField()
    pending = models.BooleanField()

class Offer(models.Model):
    gig = models.ForeignKey('Gig')
    amount = models.FloatField()
    provider = models.ForeignKey(AUTH_USER_MODEL)
    expiredate = models.DateField()
    expiretime = models.TimeField()
