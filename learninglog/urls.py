from django.conf.urls import  url
from . import views
#from django.contrib import admin
#from .learninglog import urls

urlpatterns = [
    url(r'^index/$', views.index, name = 'index'),
    url(r'^places/$', views.places, name = 'places'),
    url(r'^home/$', views.home, name='home'),
    url(r'^topics/$',views.topics, name = 'topics'),
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
    ]
