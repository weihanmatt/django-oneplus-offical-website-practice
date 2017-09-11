from django.conf.urls import include,url
from django.contrib import admin

from . import views, viewsgoods

urlpatterns = [
    #后台首页
    url(r'^$', views.index, name="myadmin_index"),


    #后台管理员路由
    url(r'^login$', views.login, name="myadmin_login"),
    url(r'^dologin$', views.dologin, name="myadmin_dologin"),
    url(r'^logout$', views.logout, name="myadmin_logout"),
    url(r'^verifycode$', views.verifycode, name="myadmin_verifycode"),


    url(r'^adduser$', views.adduser, name="myadmin_adduser"),
    url(r'^deleteuser(?P<uid>[0-9]*)$', views.deleteuser, name="myadmin_deleteuser"),
    # url(r'^browseuser$', views.browseuser, name="myadmin_browseuser"),
    url(r'^insert$', views.insertuser, name="myadmin_insertuser"),
    url(r'^edituser(?P<uid>[0-9]*)$', views.edituser, name="myadmin_edituser"),
    url(r'^updateuser(?P<uid>[0-9]*)$', views.updateuser, name="myadmin_updateuser"),
    url(r'^browseuser/(?P<pIndex>[0-9]*)$', views.browseuser, name='myadmin_browseuser'),


    #商品管理路由
    url(r'^browsegoods/(?P<pIndex>[0-9]*)$', viewsgoods.browsegoods, name='myadmin_browsegoods'),
    url(r'^addgoods$', viewsgoods.addgoods, name="myadmin_addgoods"),
    url(r'^insertgoods$', viewsgoods.insertgoods, name="myadmin_insertgoods"),
    url(r'^editgoods(?P<uid>[0-9]*)$', viewsgoods.editgoods, name="myadmin_editgoods"),
    url(r'^deletegoods(?P<uid>[0-9]*)$', viewsgoods.deletegoods, name="myadmin_deletegoods"),
    url(r'^updategoods(?P<uid>[0-9]*)$', viewsgoods.updategoods, name="myadmin_updategoods"),

    # 后台商品类别信息管理
    url(r'^type$', viewsgoods.browsetype, name="myadmin_browsetype"),
    url(r'^typeadd/(?P<tid>[0-9]+)$', viewsgoods.addtype, name="myadmin_addtype"),
    url(r'^typeinsert$', viewsgoods.inserttype, name="myadmin_inserttype"),
    url(r'^typedel/(?P<tid>[0-9]+)$', viewsgoods.deltype, name="myadmin_deltype"),
    url(r'^typeedit/(?P<tid>[0-9]+)$', viewsgoods.edittype, name="myadmin_edittype"),
    url(r'^typeupdate/(?P<tid>[0-9]+)$', viewsgoods.updatetype, name="myadmin_updatetype"),

]