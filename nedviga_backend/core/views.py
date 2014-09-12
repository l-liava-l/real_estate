# coding: utf-8

import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


class BaseView(View):

    content_type = 'application/json'

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated():
    #         return super(BaseView, self).dispatch(request, *args, **kwargs)
    #     else:
    #         return self.render_json_response(success=False, errors={'internal_error': 'auth_required'}, status=401)

    def render_json_response(self, data=None, errors=None, success=None, status=200):
        """
        Стандартная view для проекта
        """
        #если success не заполенен, то заполняем автоматически
        if not success:
            if data:
                success = True
            if errors:
                success = False
            if data and errors:
                raise Exception('Manually specify "success" arg, because both "error" and "data" are not empty')
        ctx = {
            'success': success,
            'errors': errors,
            'data': data,
        }
        json_context = json.dumps(ctx).encode('utf-8')
        response = HttpResponse(json_context, self.content_type, status=status)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'True'
        return response

    def render_internal_error(self, text):
        return self.render_json_response(errors={'internal_error': text})

    def render_empty_success(self):
        return self.render_json_response(success=True)


class BaseHTMLPage(View):
    @staticmethod
    def get(request):
        return render(request, 'base_page.html')


class RawHTMLPage(View):
    def get(self, request, template_path):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        te = os.path.join(base_dir, '../_public/www/templates/%s' % template_path)
        data = open(te, mode="r", encoding='utf-8', closefd=True).read().encode('utf-8')
        return HttpResponse(data)
