from rest_framework import serializers
from authentication.models import Profile
from authentication.repository import create_related_role


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type']

    def create(self, validated_data):
        profile = super().create(validated_data=validated_data)
        create_related_role(profile)
        return profile
