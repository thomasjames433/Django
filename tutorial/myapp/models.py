from django.db import models

# Create your models here.

class Feature:
    id: int
    name: str
    details: str
    valid: bool

class Match:
    name1: str
    name2: str
    todo: str

class Footballer(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500)