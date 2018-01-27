from django.conf.urls import  url
from . import views
#from django.contrib import admin
#from .learninglog import urls

urlpatterns = [
    url(r'^index/$', views.index, name = 'index'),
    url(r'^places/$', views.places, name = 'places'),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'', include(learninglog.urls)),
]
