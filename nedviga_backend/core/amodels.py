from django.db import models


class TimeStampModel(models.Model):
    """
    Время создания и удаления
    """
    when_created = models.DateTimeField(verbose_name='Когда создана', auto_now_add=True)
    when_modified = models.DateTimeField(verbose_name='Когда отредактирована', auto_now=True)

    class Meta:
        abstract = True