from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from authentication.models.managers import ProfileManager


class Profile(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        (1, 'developer'),
        (2, 'product_manager'),
    )
    username = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(max_length=64, unique=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone_number']
    objects = ProfileManager()