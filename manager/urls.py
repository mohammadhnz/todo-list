from django.urls import path, include
from rest_framework import routers

from manager.views.project import ProjectViewSet
from manager.views.task import DeveloperTasksViewSet, ProductManagerTaskViewSet

router = routers.DefaultRouter()
router.register(r'project', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'product-manager/tasks/<int:project_id>',
        ProductManagerTaskViewSet.as_view({
            'get': 'list',
            'post': 'create',
        })
    ),
    path(
        'product-manager/tasks/<int:project_id>/<int:pk>/',
        ProductManagerTaskViewSet.as_view({
            'get': 'retrieve',
            'patch': 'partial_update',
        })
    ),
    path(
        'developer/tasks/<int:project_id>',
        DeveloperTasksViewSet.as_view({
            'get': 'list',
            'post': 'create',
        })
    ),
    path(
        'developer/tasks/<int:project_id>/assigned/',
        DeveloperTasksViewSet.as_view({'get': 'get_tasks'})
    ),
    path(
        'developer/tasks/assign/<int:project_id>/<int:task_id>',
        DeveloperTasksViewSet.as_view({'post': 'assign'})
    ),
]
