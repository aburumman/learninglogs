from django.conf.urls import  url
from . import views
#from django.contrib import admin
#from .learninglog import urls

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^topics/$',views.topics, name = 'topics'),
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
    url(r'^new_topic/$', views.new_topic, name = 'new_topic'),
    url(r'^add_entry/(?P<topic_id>\d+)/$', views.add_entry, name = 'add_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name = 'edit_entry'),
    ]
