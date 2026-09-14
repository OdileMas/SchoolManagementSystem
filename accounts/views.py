from rest_framework import generics, permissions
from .serializers import RegisterSerializer, AdminCreateUserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class AdminCreateUserView(generics.CreateAPIView):
    serializer_class = AdminCreateUserSerializer
    permission_classes = [permissions.IsAdminUser]