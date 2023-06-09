from django.urls import path

from authentication.views.register import ProfileRegisterAPIView
from authentication.views.token_obtain import ProfileTokenObtainPairView

urlpatterns = [
    path('register/', ProfileRegisterAPIView.as_view()),
    path('login/', ProfileRegisterAPIView.as_view()),
    path('login/refresh/', ProfileTokenObtainPairView.as_view()),
]
