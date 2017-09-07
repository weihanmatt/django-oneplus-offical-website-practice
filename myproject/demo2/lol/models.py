from django.db import models

class leesin(models.Model):
	name = models.CharField(max_length=32)
	age = models.IntegerField(max_length=4)
	phone = models.CharField(max_length=16)
