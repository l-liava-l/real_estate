# coding: utf-8

from django.conf.urls import patterns, url
from .views import FilterView

urlpatterns = patterns(
    'filters.views',
    url(r'^get_list/?$', FilterView.as_view(), name='filter'),
    url(r'^save/?$', FilterView.as_view(), name='save_filter'),
)
