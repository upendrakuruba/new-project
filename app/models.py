from django.db import models

# Create your models here.
class rara(models.Model):
    Actor =models.CharField(max_length=100)
    Director =models.CharField(max_length=100)