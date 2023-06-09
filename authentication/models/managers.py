from django.contrib.auth.base_user import BaseUserManager
from rest_framework.exceptions import ValidationError


class ProfileManager(BaseUserManager):
    def _create_user(self, username, password, is_superuser=False, is_staff=False, **extra_fields):
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, is_superuser=True, is_staff=True, **extra_fields)
