from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsDM(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_dm)


"""
    permission to modify in DM, to read in authenticated
"""


class IsDMOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_dm
        )
