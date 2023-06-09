from django.db import models

from _utils.base_model import HistoricalBaseModel


class Project(HistoricalBaseModel):
    product_manager = models.ForeignKey(to='manager.ProductManager', on_delete=models.CASCADE)
    name = models.CharField(max_length=32, )
    developers = models.ManyToManyField(to='manager.Developer', related_name='projects')
