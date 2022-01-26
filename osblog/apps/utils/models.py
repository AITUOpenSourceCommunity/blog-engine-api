from django.db import models
from django.utils.translation import gettext_lazy as _


class CommonModel(models.Model):
    class Meta:
        abstract = True
        verbose_name = None
        verbose_name_plural = None

    created_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Время создания объекта")
    )
    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Время последнего обновления объекта")
    )
    objects = models.Manager()
