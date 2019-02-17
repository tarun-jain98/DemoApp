from django.conf.urls import url, include
from django.contrib import admin
# from django.contrib.auth import views
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    url(r'^home/$', views.home, name='home'),
    url(r'^delete/(?P<name>[\w\-\.]+)$', views.delete, name='delete'),
]