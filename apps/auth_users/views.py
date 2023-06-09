from knox.models import AuthToken, AuthTokenManager
from knox.views import LoginView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView

from apps.auth_users.serializers import LoginUserSerializerSchema
from apps.users.serializers import UserClientSerializer
from apps.users.values.user_type import UserType


# Create your views here.
class LoginCustomView(LoginView):
    serializer_class = LoginUserSerializerSchema
    authentication_classes = (BasicAuthentication,)


class AuthRegisterClientView(APIView):
    serializer_class = UserClientSerializer

    @staticmethod
    def post(request):
        user_serializer = UserClientSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save(user_type=UserType.CLIENT)

        token = (AuthToken.objects.create(user))[1]

        login_serializer = LoginUserSerializerSchema()

        login_data = login_serializer.data
        login_data['token'] = token
        login_data['expiry'] = None
        login_data['user'] = user_serializer.data

        return Response(login_data, status=status.HTTP_201_CREATED)
