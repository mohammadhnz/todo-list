from django.db import models

from _utils.base_model import HistoricalBaseModel


class Developer(HistoricalBaseModel):
    profile = models.OneToOneField(
        to='authentication.Profile',
        on_delete=models.CASCADE
    )


class ProductManager(HistoricalBaseModel):
    profile = models.OneToOneField(
        to='authentication.Profile',
        on_delete=models.CASCADE
    )
