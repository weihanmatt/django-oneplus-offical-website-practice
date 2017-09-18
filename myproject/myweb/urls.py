from django.conf.urls import include,url
from django.contrib import admin

from . import views,viewsorders

urlpatterns = [
    #当前应用的首页入库地址
    url(r'^$', views.index, name="index"),
    
    url(r'^oneplus5$', views.oneplus5, name="oneplus5"),
    
    
    #购物车
    url(r'^shopchart$', viewsorders.shopchart, name="shopchart"),
    url(r'^shopchartadd(?P<gid>[0-9]+)$', viewsorders.shopchartadd, name="shopchartadd"),
    url(r'^shopchartdel/(?P<gid>[0-9]+)$', viewsorders.shopchartdel,name='shopchartdel'), #从购物车中删除一个商品
    url(r'^shopchartclear$', viewsorders.shopchartclear,name='shopchartclear'), #清空购物车
    url(r'^shopchartchange$', viewsorders.shopchartchange,name='shopchartchange'), #更改购物车中商品数量

    #订单页
    url(r'^order$', viewsorders.order, name="order"),
    url(r'^orderconfirm$', viewsorders.orderconfirm, name="orderconfirm"),
    url(r'^orderinsert$', viewsorders.insertorder, name="insertorder"),



    #登录
    url(r'^login$', views.login, name="login"),
    url(r'^dologin$', views.dologin, name="dologin"),
    url(r'^verifycode$', views.verifycode, name="myweb_verifycode"),
    url(r'^logout$', views.logout, name="logout"),

    # 注册
    url(r'^register$', views.register, name="register"),
    url(r'^registuser$', views.registuser, name="registuser"),

    #个人中心
    url(r'^personal(?P<uid>[0-9]*)$', views.personal, name="personal"),
    url(r'^personalupdate(?P<uid>[0-9]*)$', views.personalupdate, name="personalupdate"),
    url(r'^personalmyorders(?P<uid>[0-9]*)$', views.myorders, name="myorders"),
    url(r'^personalorderdetail(?P<uid>[0-9]*)$', views.orderdetail, name="orderdetail"),
    url(r'^personalsafe$', views.safe, name="safe"),
    url(r'^personalchange$', views.changepassword, name="changepassword"),


    #商品列表页
    url(r'^mall$', views.mall, name="mall"),
    url(r'^details(?P<gid>[0-9]+)$', views.details, name="details"),
    url(r'^list(?P<tid>[0-9]+)$', views.list, name="list"), #带参数列表页

]