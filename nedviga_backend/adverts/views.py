# coding: utf-8

import random

from core.views import BaseView


class ListAdverts(BaseView):
    def get(self, request):
        results = []
        count = 0
        for x in range(10):
            count += 1
            result = {
                "count": count,
                "type": "Жилой гараж",
                "address": "Каштаянца 15, кв. 80",
                "cost": "{0} сутки".format(random.randint(500, 15000)),
                "description": "ОТ СОБСТВЕННИКА.Звонить можно круглосуточно.Сдается комната посуточно в квартире , со всеми удобствами, с евроремонтом и новой мебелью. Для вашего комфортного проживания                            ЖК телевизор, спутниковое ТВ.                           Все входит в стоимость проживания Заселение круглосуточно.Без комиссий, предоплат и залога.",
                "images": ['http://lorempixel.com/512/512/' for x in range(random.randint(2, 6))],
                "numbers": ['8 (900) 000 00 00' for x in range(random.randint(0, 4))],
            }
            results.append(result)
        return self.render_json_response(results)
