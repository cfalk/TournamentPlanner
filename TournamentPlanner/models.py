from django.db import models
from django.contrib.auth.models import User

class Tournament(models.Model):
 name = models.CharField(max_length=60)
 date = models.DateField()
 user = models.ForeignKey(User)
 rounds_passed = models.IntegerField(default=0)

class Participant(models.Model):
 name= models.CharField(max_length=60)
 tournament = models.ForeignKey(Tournament)
 losses = models.IntegerField(default=0)
 wins = models.IntegerField(default=0)
 
