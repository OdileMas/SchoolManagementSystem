from rest_framework.permissions import BasePermission


class IsRoleAdmin(BasePermission):
    """
    Allows access only to authenticated users whose custom `role` field is ADMIN.
    """
    message = "Only users with role=ADMIN can perform this action."

    def has_permission(self, request, view):
        user = request.user
        return bool(
            user
            and user.is_authenticated
            and getattr(user, "role", None) == user.ADMIN
        )