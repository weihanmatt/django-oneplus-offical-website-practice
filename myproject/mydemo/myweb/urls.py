# -*- coding: utf-8 -*-
# 
from django.conf.urls import url
from . import views,pic

urlpatterns = [
    url(r'^$', views.index, name="index"),

    #使用session实现简单购物车
    url(r'^shop$', views.shop,name='shop'), #浏览商品
    url(r'^addshop$', views.addshop,name='addshop'), #添加购物车
    url(r'^showshop$', views.showshop,name='showshop'), #浏览购物车
    url(r'^delshop/(?P<shopid>[0-9]{4})$', views.delshop,name='delshop'), #从购物车中删除一个商品
    url(r'^clearshop$', views.clearshop,name='clearshop'), #清空购物车
    url(r'^changeshop$', views.changeshop,name='changeshop'), #更改购物车中商品数量


    # 验证码的输出
    url(r'^showcode$', views.showcode,name='showcode'),
    url(r'^login$', views.login,name='login'),

    # 相册图片信息管理
    url(r'^pic$', pic.indexpic, name="pic"), #浏览相册图片信息
    url(r'^pic/add$', pic.addpic, name="addpic"), #加载添加相册图片信息表单
    url(r'^pic/insert$', pic.insertpic, name="insertpic"), #执行相册图片信息添加
    url(r'^pic/(?P<uid>[0-9]+)/del$', pic.delpic, name="delpic"), #执行相册图片信息删除
    url(r'^pic/(?P<uid>[0-9]+)/edit$', pic.editpic, name="editpic"), #加载相册图片信息编辑表单
    url(r'^pic/update$', pic.updatepic, name="updatepic"), #执行相册图片信息编辑

]
