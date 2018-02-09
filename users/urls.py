from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name':'users/login.html'}, name = 'login'),
    url(r'^logout/$', views.logout_user, name = 'logout'),
    url(r'sign_up/$', views.sign_up, name = 'sign_up'),
]
