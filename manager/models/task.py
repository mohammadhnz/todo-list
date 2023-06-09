from django.db import models

from _utils.base_model import HistoricalBaseModel


class Task(HistoricalBaseModel):
    title = models.CharField(max_length=128)
    project = models.ForeignKey(to='manager.Project', on_delete=models.CASCADE)
    assignees = models.ManyToManyField(to='manager.Developer', related_name='tasks')
