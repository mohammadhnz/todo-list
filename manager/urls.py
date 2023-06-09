from rest_framework import routers
from django.urls import path, include
from manager.views.project import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'project', ProjectViewSet, basename='project')


urlpatterns = [path('', include(router.urls))]