# coding: utf-8

from django.conf.urls import patterns, url
from .views import PreLogin, Login, SessionidView

urlpatterns = patterns(
    'authentication.views',
    url(r'^sessionid/?$', SessionidView.as_view(), name='sessionid'),
    url(r'^prelogin/?$', PreLogin.as_view(), name='prelogin'),
    url(r'^login/?$', Login.as_view(), name='login'),
)
