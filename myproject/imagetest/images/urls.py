from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'pic^$',views.index,name="index"),
	url(r'^add$',views.addPic,name="addPic"),
	url(r'^insert$',views.insertPic,name="insertPic"),
	url(r'^(?P<uid>[0-9]+)/del$',views.delpic,name="delpic"),




]