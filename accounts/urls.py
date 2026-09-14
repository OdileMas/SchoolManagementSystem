from django.urls import path
from rest_framework_simplejwt.views import  TokenRefreshView
from .views import RegisterView, AdminCreateUserView, CustomTokenObtainPairView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("admin/create-user/", AdminCreateUserView.as_view(), name="admin-create-user"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]