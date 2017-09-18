from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(max_length=1)
    code = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    status = models.IntegerField(max_length=1)
    addtime = models.IntegerField(max_length=11)

class Goods(models.Model):
    typeid = models.IntegerField(max_length=11)
    goods = models.CharField(max_length=32)
    company = models.CharField(max_length=50)
    descr = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    picname = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    store = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    addtime = models.IntegerField(max_length=20)

    def toDict(self):
        return {'id':self.id,'goods':self.goods,'price':self.price,'picname':self.picname,'store':self.store,'num':self.num}

#商品类别信息模型
class Types(models.Model):
    name = models.CharField(max_length=32)
    pid = models.IntegerField(default=0)
    path = models.CharField(max_length=255)



class Order(models.Model):
    uid = models.IntegerField(max_length=11)
    linkman = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    addtime = models.IntegerField(max_length=11)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.IntegerField(default=0)
    # goods = models.CharField(max_length=32)

class Detail(models.Model):
    orderid = models.IntegerField(max_length=11)
    goodsid = models.IntegerField(max_length=11)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    num = models.IntegerField(max_length=11)
    goodsname = models.CharField(max_length=32)
    picname = models.CharField(max_length=32)









