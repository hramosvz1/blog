from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^$', views.index, name=u'index'),
	url(r'^acerca/$', views.about, name=u'about'),
	url(r'^contacto/$', views.contact, name=u'contact'),
	url(r'^categoria/(?P<slug>[-\w]+)/$', views.category, name=u'category'),
	url(r'^categoria/(?P<slug>[-\w]+)/(?P<pk>\d+)/$', views.post, name=u'post'),
	url(r'^login/$', views.login, name=u'login'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)