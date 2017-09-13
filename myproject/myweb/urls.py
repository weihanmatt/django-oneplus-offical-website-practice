from django.conf.urls import include,url
from django.contrib import admin

from . import views

urlpatterns = [
    #当前应用的首页入库地址
    url(r'^$', views.index, name="index"),
    
    url(r'^oneplus5$', views.oneplus5, name="oneplus5"),
    
    
    
    url(r'^shopchart$', views.shopchart, name="shopchart"),

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
    url(r'^list(?P<tid>[0-9]+)$', views.list, name="list"), #带参数列表页
]