from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)

class IsProjectManager(BasePermission):
    """
    Allows access only to project manager users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_project_manager)

class IsDemandManager(BasePermission):
    """
    Allows access only to demand manager users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_demand_manager)

class IsAdminOrIsSelfUser(BasePermission):
    """
    Allows access to self users or admin(useful to self user data update).
    """

    def has_permission(self, request, view):
        detail = int(request.parser_context['kwargs']['pk'])

        return (
            (request.user and request.user.id == detail) or
            (request.user and request.user.is_admin)
        )
