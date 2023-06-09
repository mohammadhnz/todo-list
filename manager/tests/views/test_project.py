from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from authentication.models import Profile
from manager.models import Project, ProductManager
from manager.serializers.project_serializers import ProjectListRetrieveSerializer


class ProjectViewSetTestCase(TestCase):
    def setUp(self):
        # Create a user with account type 2
        self.profile = Profile.objects.create_user(
            username='user1', password='pass123', user_type=2)
        self.product_manager = ProductManager.objects.create(profile=self.profile)
        self.project = Project.objects.create(product_manager=self.product_manager)
        self.client = APIClient()
        token = self.client.post(
            '/login/', {
                'username': 'user1',
                'password': 'pass123',
            }
        ).json()['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_project_list_retrieve(self):
        response = self.client.get(reverse('project-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
