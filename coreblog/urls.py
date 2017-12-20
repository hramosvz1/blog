from django.conf.urls import url,include
from django.contrib import admin
from . import views



urlpatterns = [
	url(r'^$', views.index, name=u'index'),
	url(r'^about/$', views.about, name=u'about'),
	url(r'^contact/$', views.contact, name=u'contact'),
	url(r'^post/$', views.post, name=u'post'),


]