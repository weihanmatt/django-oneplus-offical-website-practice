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


    #登录
    url(r'^login$', views.login, name="login"),
    url(r'^dologin$', views.dologin, name="dologin"),
    url(r'^verifycode$', views.verifycode, name="myweb_verifycode"),
    url(r'^logout$', views.logout, name="logout"),

    # 注册
    url(r'^register$', views.register, name="register"),
    url(r'^registuser$', views.registuser, name="registuser"),

    #商品列表页
    url(r'^mall$', views.mall, name="mall"),
    url(r'^details(?P<gid>[0-9]+)$', views.details, name="details"),
    url(r'^list(?P<tid>[0-9]+)$', views.list, name="list"), #带参数列表页

]