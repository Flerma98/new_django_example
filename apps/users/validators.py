from django.contrib.auth import password_validation
from django.core import exceptions
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator


# my validators here:
class UniqueUsernameValidator(UniqueValidator):
    message = 'Nombre de usuario ya esta siendo usado por otro usuario'


class UniqueEmailValidator(UniqueValidator):
    message = 'Correo electrónico ya esta siendo usado por otro usuario'


class TokenPasswordValidator(object):
    message_expire = 'El token a expirado'
    message_not_found = 'El token no existe'

    def __init__(self, queryset):
        self.qs = queryset

    def __call__(self, value):
        try:
            token = self.qs.get(key=value)
            # check if it is still valid
            if token.expire():
                raise ValidationError(self.message_expire, code='expire')
        except exceptions.ObjectDoesNotExist:
            raise ValidationError(self.message_not_found, code='not_found')


class PasswordStrengthValidator(object):
    def __init__(self, user=None):
        self.user = user

    def __call__(self, value):
        password_validation.validate_password(password=value, user=self.user)


class CanEditPermissions(object):
    error_messages = {
        'superuser': {
            'detail': 'El usuario dado es un super usuario, y no puedes editar'
                      ' super usuarios.',
            'code': 'cannot_edit_superuser',
        },
        'not_staff': {
            'detail': 'El usuario dado no es un administrador',
            'code': 'cannot_edit_normal_user',
        },
        'no_permissions': {
            'detail': 'El usuario dado no tiene una instancia de permisos,'
                      'por favor de reportar este incidente a un desarrollador'
                      ' de la API.',
            'code': 'cannot_edit_without_permissions',
        },
    }

    def __call__(self, value):
        error = None
        if value.is_superuser:
            error = self.error_messages['superuser']
        elif not value.is_staff:
            error = self.error_messages['not_staff']
        elif not hasattr(value, 'permissions'):
            error = self.error_messages['no_permissions']
        if error:
            raise ValidationError(**error)