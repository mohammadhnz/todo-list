from rest_framework import permissions


class IsDeveloper(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            get_account.get_developer(request.user)
            return True
        except:
            return False


class IsProductManager(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            get_account.get_product_manager(request.user)
            return True
        except:
            return False


class IsProjectOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            manager = get_account.get_product_manager(request.user)
            project_id = view.kwargs.get('project_id')
            if repository.get_product_manager_project(manager_id=manager.id, id=project_id):
                return True
            raise exceptions.AccountIsNotProjectManagerError(
                f'Manager with ID: {manager.id} has not permission to project with ID: {project_id}')
        except:
            return False


class IsProjectMember(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            developer = get_account.get_developer(request.user)
            project_id = view.kwargs.get('project_id')
            project = repository.get_project_by_id(project_id=project_id)

            if project.developers.filter(id=developer.id).exists():
                return True
            raise exceptions.AccountIsNotProjectDeveloperError(
                f'Developer with ID: {developer.id} is not member of project with ID: {project_id}')
        except:
            return False
