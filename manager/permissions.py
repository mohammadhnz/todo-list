from rest_framework import permissions

from authentication.services.account import get_product_manager_by_profile, get_developer_by_profile
from manager.repository import get_project_managers_id, get_project_by_id, is_developer_part_of_project


class IsProjectManager(permissions.BasePermission):
    def has_permission(self, request, view):
        product_manager = get_product_manager_by_profile(request.user)
        if not product_manager:
            return False
        project_id = view.kwargs.get('project_id')
        if get_project_managers_id(project_id) == product_manager.id:
            return True
        return False


class IsProjectDeveloper(permissions.BasePermission):
    def has_permission(self, request, view):
        developer = get_developer_by_profile(request.user)
        if not developer:
            return False
        project_id = view.kwargs.get('project_id')
        if is_developer_part_of_project(developer, project_id):
            return True
