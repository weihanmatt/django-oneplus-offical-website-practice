from django.conf.urls import include,url
from django.contrib import admin

from . import views

urlpatterns = [
    #后台首页
    url(r'^$', views.index, name="myadmin_index"),


    #后台管理员路由
    url(r'^login$', views.login, name="myadmin_login"),
    url(r'^dologin$', views.dologin, name="myadmin_dologin"),
    url(r'^logout$', views.logout, name="myadmin_logout"),


    url(r'^adduser$', views.adduser, name="myadmin_adduser"),
    url(r'^deleteuser(?P<uid>[0-9]*)$', views.deleteuser, name="myadmin_deleteuser"),
    # url(r'^browseuser$', views.browseuser, name="myadmin_browseuser"),
    url(r'^insert$', views.insertuser, name="myadmin_insertuser"),
    url(r'^edituser(?P<uid>[0-9]*)$', views.edituser, name="myadmin_edituser"),
    url(r'^updateuser(?P<uid>[0-9]*)$', views.updateuser, name="myadmin_updateuser"),
    url(r'^browseuser/(?P<pIndex>[0-9]*)$', views.browseuser, name='myadmin_browseuser'),

]