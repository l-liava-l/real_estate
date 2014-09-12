# coding: utf-8
from django.conf import settings


class SessionUrlHackMiddleware(object):

    def process_request(self, request):
        raw_session_key = request.GET.get(settings.SESSION_COOKIE_NAME)
        if raw_session_key:
            request.COOKIES[settings.SESSION_COOKIE_NAME] = raw_session_key
