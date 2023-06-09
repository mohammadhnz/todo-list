from rest_framework.generics import CreateAPIView

from authentication.serializers.profile import ProfileSerializer


class ProfileRegisterAPIView(CreateAPIView):
    serializer_class = ProfileSerializer
