from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authentication.permissions import IsProductManager, IsDeveloper
from authentication.services.account import get_developer_by_profile
from manager.permissions import IsProjectManager, IsProjectDeveloper
from manager.repository import get_project_tasks, assign_task_to_developer, get_developers_project_tasks
from manager.serializers.task_serializers import TaskListRetrieveSerializer, TaskCreateUpdateSerializer


class ProductManagerTaskViewSet(ModelViewSet):
    permission_classes = [IsProductManager, IsProjectManager]

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return TaskCreateUpdateSerializer
        return TaskListRetrieveSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        return get_project_tasks(project_id)


class DeveloperTasksViewSet(ProductManagerTaskViewSet):
    permission_classes = [IsDeveloper, IsProjectDeveloper]

    def get_queryset(self):
        if self.action == 'get_tasks':
            developer = get_developer_by_profile(self.request.user)
            project_id = self.kwargs.get('project_id')
            return get_developers_project_tasks(developer, project_id)
        return super().get_queryset()

    def assign(self, *args, task_id, **kwargs):
        developer = get_developer_by_profile(self.request.user)
        assign_task_to_developer(task_id, developer)
        return Response(status=status.HTTP_200_OK)

    def get_tasks(self, *args, **kwargs):
        return super().list(*args, **kwargs)
