import base64

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def login(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    if not auth_header or not auth_header.startswith('Basic '):
        return Response(_('Credentials was not provided'), status=status.HTTP_401_UNAUTHORIZED)

    credentials = auth_header[len('Basic '):].strip()
    credentials = base64.b64decode(credentials).decode('utf-8')
    username, password = credentials.split(':', 1)

    user = authenticate(request, username=username, password=password)
    if user is None:
        return Response(_('Invalid credentials'), status=status.HTTP_401_UNAUTHORIZED)

    return Response(user, status=status.HTTP_200_OK)
