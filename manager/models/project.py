from django.db import models

from _utils.base_model import HistoricalBaseModel


class Project(HistoricalBaseModel):
    product_manager = models.ForeignKey(to='manager.ProductManager', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=32, )
    developers = models.ManyToManyField(to='to_do.Developer', related_name='projects')