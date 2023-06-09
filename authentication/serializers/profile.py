from rest_framework import serializers
from authentication.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type']