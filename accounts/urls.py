from django.urls import path
from .views import RegisterView,  AdminCreateUserView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("admin/create-user/", AdminCreateUserView.as_view(), name="admin-create-user"),
]