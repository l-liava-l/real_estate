# coding: utf-8

from core.views import BaseView
from adverts.models import Advert


class FilterView(BaseView):
    def get(self, request):
        filter_id = int(request.GET.get('filter_id'))
        user = request.user
        adverts = Advert.objects.filter(useradvert__filter__id=filter_id, useradvert__filter__user__id=user.id)
        adverts_list = []
        for advert in adverts:
            adverts_list.append(advert.serialize_to_dict())
        return self.render_json_response(data=adverts_list)

    def post(self, request):
        print(request)
