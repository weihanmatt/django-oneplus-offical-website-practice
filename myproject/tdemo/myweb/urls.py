from django.conf.urls import include,url
from django.contrib import admin

from . import views

urlpatterns = [
    #当前应用的首页入库地址
    url(r'^$', views.index, name="index"),
    
    #测试模板标签
    url(r'^tpl01$', views.tpl01, name="tpl01"),
    url(r'^oneplus$', views.opIndex, name="opIndex"),
]
