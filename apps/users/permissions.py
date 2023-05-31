from django.utils.translation import gettext
from rest_framework.permissions import BasePermission

from apps.users.models import User
from apps.users.values.user_type import UserType


class BaseUserPermission(BasePermission):
    field = ''  # type: str
    verbose_name = ''

    @property
    def message(self):
        return gettext(
            'User %(user)s must have permission for %(permission)s'
            ' in order to perform this action.'
        ) % {
            'user': getattr(self, 'user', 'not_found'),
            'permission': self.verbose_name if self.verbose_name else self.field
        }

    @staticmethod
    def _permission_get(user, attr):
        if not hasattr(user, 'permissions'):
            return False
        return getattr(user.permissions, attr, False)

    def has_permission(self, request, view):
        assert self.field, (
                '`%s` attribute `field` was not set up, you must give the field that we'
                ' need to check' % self.__class__.__name__
        )
        user = request.user
        setattr(self, 'user', str(user))

        if user.is_superuser:
            return True
        else:
            return self._permission_get(user, self.field)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == UserType.ADMIN


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj: User):
        return obj == request.user


class IsAdminOrIsTheOwner(BasePermission):
    def has_object_permission(self, request, view, obj: User):
        if request.user.user_type == UserType.ADMIN:
            return True
        return obj == request.user
