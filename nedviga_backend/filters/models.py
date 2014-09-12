from django.db import models

from adverts.amodels import AbstractAdvert
from core.amodels import TimeStampModel


class Filter(AbstractAdvert, TimeStampModel):
    user = models.ForeignKey('authentication.User', verbose_name='Пользователь')
    name = models.CharField('Название', null=False, blank=False, max_length=50)

    price_min = models.PositiveIntegerField('Нижняя граница цены', blank=True, null=True)
    price_max = models.PositiveIntegerField('Верхняя граница цены', blank=True, null=True)

    class Meta:
        verbose_name = 'Пользовательский фильтр'
        verbose_name_plural = 'Пользовательские фильтры'
        ordering = ('-id',)

    def __str__(self):
        return str(self.id)


class UserAdvert(TimeStampModel):
    filter = models.ForeignKey('Filter', verbose_name='Фильтр')
    advert = models.ForeignKey('adverts.Advert', verbose_name='Объявление')
    is_read = models.BooleanField('Прочитано?', default=False)

    class Meta:
        verbose_name = 'Объявление, подходящее под фильтр'
        verbose_name_plural = 'Объявления, подходящие под фильтр'
        ordering = ('-id',)
        unique_together = ('filter', 'advert')

    def __str__(self):
        return '{} фильтр {} объявление {}'.format(self.id, self.filter_id, self.advert_id)

