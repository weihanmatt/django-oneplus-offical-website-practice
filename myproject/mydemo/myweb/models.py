# -*- coding: utf-8 -*-
# 
from django.db import models

# Create your models here.
class Stu(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField(default=20)
    sex = models.CharField(max_length=1)
    classid = models.CharField(max_length=8)

class District(models.Model):
	name = models.CharField(max_length=255)
	upid = models.IntegerField()

class Pic(models.Model):
	name = models.CharField(max_length=32)
	age = models.IntegerField()
	picname = models.CharField(max_length=32)
	addtime = models.IntegerField()
