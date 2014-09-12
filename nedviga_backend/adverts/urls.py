# coding: utf-8

from django.conf.urls import patterns, url
from .views import ListAdverts

urlpatterns = patterns(
    'adverts.views',
    url(r'random/?$', ListAdverts.as_view(), name='list_random_adverts'),
)
