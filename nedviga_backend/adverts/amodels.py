from django.db import models
from bitfield import BitField
from djorm_pgarray.fields import IntegerArrayField


class AbstractAdvert(models.Model):
    is_rent = models.BooleanField('True = аренда, False = продажа', default=True)
    SECTION_APARTMENT = 1
    SECTION_HOUSE = 2
    SECTION_NOT_LIVE = 3
    SECTION_CHOICES = (
        (SECTION_APARTMENT, 'Квартира'),
        (SECTION_HOUSE, 'Дом, коттедж'),
        (SECTION_NOT_LIVE, 'Нежилое помещение'),
    )
    section = models.PositiveSmallIntegerField('Тип помещения', choices=SECTION_CHOICES)
    section_additional = BitField(flags=range(1, 60))

    additional_requirements = BitField(flags=range(1, 60))

    metro = IntegerArrayField()

    class Meta:
        abstract = True
