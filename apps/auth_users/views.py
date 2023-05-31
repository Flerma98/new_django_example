from knox.views import LoginView
from rest_framework.authentication import BasicAuthentication

from apps.auth_users.serializers import LoginUserSerializerSchema


# Create your views here.
class LoginCustomView(LoginView):
    serializer_class = LoginUserSerializerSchema
    authentication_classes = (BasicAuthentication,)
