from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.PositiveSmallIntegerField()
    gender = models.BooleanField()
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    goal = models.CharField(max_length=20)
    activity = models.CharField(max_length=20)
    wrist = models.PositiveSmallIntegerField()
    