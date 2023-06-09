from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views.register import ProfileRegisterAPIView
from authentication.views.token_obtain import ProfileTokenObtainPairView

urlpatterns = [
    path('register/', ProfileRegisterAPIView.as_view()),
    path('login/', ProfileTokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
]
