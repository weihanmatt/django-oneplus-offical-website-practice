from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(max_length=1)
    code = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    status = models.IntegerField(max_length=1)
    addtime = models.IntegerField(max_length=11)

class Goods(models.Model):
	typeid = models.IntegerField(max_length=11)
	goods = models.CharField(max_length=32)
	company = models.CharField(max_length=50)
	descr = models.TextField(max_length=500)
	price = models.FloatField(max_length=6)
	picname = models.CharField(max_length=255)
	status = models.IntegerField(max_length=1)
	store = models.IntegerField(max_length=11)
	num = models.IntegerField(max_length=11)
	clicknum = models.IntegerField(max_length=0)
	addtime = models.IntegerField(max_length=0)