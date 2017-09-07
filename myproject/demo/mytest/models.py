from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=16)
    
    def __str__(self):
        return self.name+":"+self.phone
