from django.core.exceptions import ValidationError
from rest_framework import serializers

from manager import repository
from manager.models import Task
from manager.repository import get_developers_by_id, get_invalid_developers_for_project


class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    developer_ids = serializers.ListSerializer(write_only=True, child=serializers.IntegerField())

    class Meta:
        model = Task
        fields = (
            'title',
            'developer_ids',
            'project',
        )

    def validate(self, attrs):
        project = attrs.get('project')
        developer_ids = attrs.get('developer_ids', [])
        if get_invalid_developers_for_project(project, developer_ids):
            raise ValidationError(
                f'You can only assign project developers to its tasks'
            )
        return attrs

    def create(self, validated_data):
        developer_ids = validated_data.pop('developer_ids', [])
        task = super().create(validated_data)
        developers = get_developers_by_id(developer_ids)
        task.assignees.set(developers)
        return task

    def update(self, instance, validated_data):
        developer_ids = validated_data.pop('developer_ids', [])
        task = super().update(instance, validated_data)
        developers = get_developers_by_id(developer_ids)
        task.assignees.set(developers)
        return task


class TaskListRetrieveSerializer(serializers.ModelSerializer):
    developers = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'developers',
        )
        read_only_fields = (
            'id',
            'title',
            'developers',
        )

    def get_developers(self, task):
        return task.assignees.all().values_list('profile__first_name', flat=True)
