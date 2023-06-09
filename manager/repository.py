from typing import List

from manager.models import Developer, ProductManager, Project


def get_developers_by_id(developers_ids: List[int]):
    return Developer.objects.filter(profile__id__in=developers_ids)


def _get_product_manager_projects(product_manager: ProductManager):
    return Project.objects.filter(product_manager=product_manager)


def get_product_manager_projects(product_manager: ProductManager):
    return _get_product_manager_projects(product_manager).prefetch_related(
        'developers',
        'developers__account',
    )


def get_invalid_developers_for_project(project, developer_ids):
    project_developer_ids = project.developers.values_list('id', flat=True)
    Developer.objects.filter(
        profile__id__in=developer_ids
    ).exclude(
        profile__id__in=project_developer_ids
    )
    project
