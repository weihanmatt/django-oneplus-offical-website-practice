from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^users$', views.indexUsers, name="users"), #浏览用户信息
    url(r'^users/add$', views.addUsers, name="addusers"), #加载添加用户信息表单
    url(r'^users/insert$', views.insertUsers, name="insertusers"), #执行用户信息添加
    url(r'^users/(?P<uid>[0-9]+)/del$', views.delUsers, name="delusers"), #执行用户信息删除
    url(r'^users/(?P<uid>[0-9]+)/edit$', views.editUsers, name="editusers"), #加载用户信息编辑表单
    url(r'^users/(?P<uid>[0-9]+)/update$', views.updateUsers, name="updateusers"), #执行用户信息编辑
    url(r'^users/file$', views.upload, name="upload"),
    url(r'^users/addfile$', views.addfile, name="addfile")
]
