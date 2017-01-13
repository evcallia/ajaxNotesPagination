from django.conf.urls import url
from . import views                   #add this line

urlpatterns = [
  url(r'^$', views.index, name='index'),  #this matches the "/" pathway
  url(r'^notes$', views.showNotes, name = 'showNotes'),   #this matches the "/users" pathway
  url(r'^create$', views.create, name = 'create'),
  url(r'^update/(?P<id>\d+)$', views.update, name = 'update'),
  url(r'^delete/(?P<id>\d+)$', views.delete, name = 'delete'),
  url(r'^pages/(?P<number>\d+)/(?P<page>\d+)$', views.pages, name = 'pages')
]
