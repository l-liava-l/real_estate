# coding: utf-8

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    'core.views',
    url(r'^$', TemplateView.as_view(template_name='frontend_docs/base.html'), name='base'),
    url(r'^authentication/?$', TemplateView.as_view(template_name='frontend_docs/auth.html'), name='auth'),
    url(r'^adverts/?$', TemplateView.as_view(template_name='frontend_docs/adverts.html'), name='adverts'),
)
