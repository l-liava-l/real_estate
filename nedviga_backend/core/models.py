from django.db import models
from core.amodels import TimeStampModel


class Settings(TimeStampModel):
    """
    Настройки
    """
    key = models.CharField(verbose_name='Ключ', max_length=255, unique=True)
    value = models.CharField(verbose_name='Значение', max_length=500)

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
        ordering = ('key',)

    def __str__(self):
        return '{0}. {1} - {2}'.format(self.pk, self.key, self.value)
