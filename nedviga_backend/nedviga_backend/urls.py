# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import BaseHTMLPage, RawHTMLPage

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(
        r'^templates/(?P<template_path>[\w\-\.\/]+)',
        RawHTMLPage.as_view(),
        name='raw_html'
    ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^frontend_docs/', include('core.urls', namespace='frontend_docs')),
    url(r'^api/adverts/', include('adverts.urls', namespace='adverts')),
    url(r'^api/filters/', include('filters.urls', namespace='filters')),
    url(r'^api/authentication/', include('authentication.urls', namespace='authentication')),
)

urlpatterns += patterns(
    '',
    url(r'', BaseHTMLPage.as_view(), name='base_page'),
)
