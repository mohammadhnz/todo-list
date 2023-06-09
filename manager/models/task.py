from django.db import models

from _utils.base_model import HistoricalBaseModel


class Task(HistoricalBaseModel):
    title = models.CharField(max_length=128)
    project = models.ForeignKey(to='to_do.Project', on_delete=models.CASCADE)
    assignees = models.ManyToManyField(to='to_do.Developer', related_name='tasks')
