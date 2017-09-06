from django.conf.urls import include,url
from django.contrib import admin

from . import views

urlpatterns = [
    #当前应用的首页入库地址
    url(r'^$', views.index, name="index"),
    url(r'^mall$', views.mall, name="mall"),
    url(r'^oneplus5$', views.oneplus5, name="oneplus5"),
    url(r'^login$', views.login, name="login"),
    url(r'^register$', views.register, name="register"),

    
    #测试模板标签
    # url(r'^oneplus$', views.opIndex, name="opIndex"),
]