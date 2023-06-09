from rest_framework.viewsets import ModelViewSet

from authentication.permissions import IsProductManager
from authentication.services.account import get_product_manager_by_profile
from manager.repository import get_product_manager_projects
from manager.serializers.project_serializers import ProjectCreateUpdateSerializer, ProjectListRetrieveSerializer


class ProjectViewSet(ModelViewSet):
    permission_classes = (IsProductManager,)

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return ProjectCreateUpdateSerializer
        return ProjectListRetrieveSerializer

    def get_queryset(self):
        product_manager = get_product_manager_by_profile(self.request.user)
        return get_product_manager_projects(product_manager)
