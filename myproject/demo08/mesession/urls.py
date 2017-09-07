from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^stu/(?P<pIndex>[0-9]*)/$', views.stu, name='stu'),
	url(r'^showdistrict$', views.showdistrict, name='showdistrict'),
    url(r'^district/([0-9]+)$', views.district, name='district'),
]