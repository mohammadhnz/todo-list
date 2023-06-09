from typing import List

from manager.models import Developer, ProductManager, Project, Task


def get_developers_by_id(developers_ids: List[int]):
    return Developer.objects.filter(profile__id__in=developers_ids)


def _get_product_manager_projects(product_manager: ProductManager):
    return Project.objects.filter(product_manager=product_manager)


def get_product_manager_projects(product_manager: ProductManager):
    return _get_product_manager_projects(product_manager).prefetch_related(
        'developers',
        'developers__account',
    )


def _get_project_tasks(project: Project):
    return Task.objects.filter(project=project)


def get_project_tasks(project_id):
    project = Project.objects.get(id=project_id)
    return _get_project_tasks(project).prefetch_related(
        'assignees',
        'assignees__account',
    )


def get_invalid_developers_for_project(project, developer_ids):
    project_developer_ids = project.developers.values_list('id', flat=True)
    return Developer.objects.filter(
        profile__id__in=developer_ids
    ).exclude(
        profile__id__in=project_developer_ids
    )


def get_project_managers_id(project_id):
    return Project.objects.get(id=project_id).product_manager_id


def get_project_by_id(project_id):
    return Project.objects.get(id=project_id)


def is_developer_part_of_project(developer_id, project_id):
    project = get_project_by_id(project_id)
    return project.developers.filter(id=developer_id).exists()


def assign_task_to_developer(task_id, developer):
    task = Task.objects.get(id=task_id)
    task.developers.add(developer)


def get_developers_project_tasks(developer, project_id):
    return developer.tasks.filter(project_id=project_id)
