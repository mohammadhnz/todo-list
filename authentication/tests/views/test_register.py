from django.test import TestCase
from rest_framework.test import APIClient

from authentication.models import Profile


class ProfileRegisterAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_profile_works_correctly(self):
        data = {
            'username': 'ali_hnz',
            'first_name': 'Ali',
            'last_name': 'HNZ',
            'email': 'alihnz@gmail.com',
            'phone_number': '1234567890',
            'user_type': 1
        }
        response = self.client.post('/register/', data)

        self.assertEqual(response.status_code, 201)

        self.assertTrue(Profile.objects.exists())

        profile = Profile.objects.get(username='ali_hnz')

        self.assertEqual(profile.username, 'ali_hnz')
        self.assertEqual(profile.first_name, 'Ali')
        self.assertEqual(profile.last_name, 'HNZ')
        self.assertEqual(profile.email, 'alihnz@gmail.com')
        self.assertEqual(profile.phone_number, '1234567890')
        self.assertEqual(profile.user_type, 1)
