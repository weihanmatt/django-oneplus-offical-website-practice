from django.db import models

# Create your models here.
class Pic(models.Model):
	name = models.CharField(max_length=16)
	age = models.IntegerField(max_length=4)
	picname = models.CharField(max_length=32)