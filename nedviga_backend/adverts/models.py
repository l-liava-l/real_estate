from django.db import models

from django.forms import model_to_dict
from .amodels import AbstractAdvert
from core.amodels import TimeStampModel


class Advert(AbstractAdvert, TimeStampModel):
    cian_id = models.BigIntegerField('id на cian.ru ', unique=True, db_index=True)
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Цена', default=0)

    PERIOD_DAY = 1
    PERIOD_MONTH = 30
    PERIOD_CHOICES = (
        (PERIOD_DAY, 'в день'),
        (PERIOD_MONTH, 'в месяц'),
    )
    price_period = models.PositiveSmallIntegerField('Период оплаты', choices=PERIOD_CHOICES, null=True, blank=True)

    storey = models.SmallIntegerField('Этаж', null=True, blank=True)
    number_of_storeys = models.SmallIntegerField('Этажность', null=True, blank=True)
    area_all = models.PositiveIntegerField('Общая площадь', null=True, blank=True)
    area_kitchen = models.PositiveIntegerField('Площадь кухни', null=True, blank=True)
    area_living = models.PositiveIntegerField('Жилая площадь', null=True, blank=True)
    area_rooms = models.PositiveIntegerField('Площадь комнат', null=True, blank=True)

    class Meta:
        verbose_name = 'Объяление'
        verbose_name_plural = 'Объявления'
        ordering = ('-id',)

    def __str__(self):
        return str(self.id)

    def serialize_to_dict(self):
        base_fields = ['id', 'is_rent', 'price_min', 'price_max']
        if self.section == self.SECTION_HOUSE:
            house_fields = ['furniture', 'tv', 'balcony', 'kitchen_furniture', 'fridge', 'animals',
                            'phone', 'washing_machine', 'children']
            base_fields += house_fields
        fields_dict = model_to_dict(self, fields=base_fields)
        fields_dict['section'] = self.get_section_display()
        return fields_dict
