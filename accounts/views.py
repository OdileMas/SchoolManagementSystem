from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    RegisterSerializer,
    AdminCreateUserSerializer,
    CustomTokenObtainPairSerializer,
)
from .permissions import IsRoleAdmin


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class AdminCreateUserView(generics.CreateAPIView):
    serializer_class = AdminCreateUserSerializer
    permission_classes = [IsRoleAdmin]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]