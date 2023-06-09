from rest_framework import permissions

from authentication.services.account import get_developer_by_profile, get_product_manager_by_profile


class IsDeveloper(permissions.BasePermission):
    def has_permission(self, request, view):
        if get_developer_by_profile(request.user):
            return True
        return False


class IsProductManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if get_product_manager_by_profile(request.user.id):
            return True
        return False
