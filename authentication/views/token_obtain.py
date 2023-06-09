from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.serializers.refresh_token import TokenObtainSerializer


class ProfileTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainSerializer
