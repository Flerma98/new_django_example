from django.urls import re_path, path

from apps.auth_users.views import AuthRegisterClientView, LoginCustomView, LogoutCustomView, LogoutAllCustomView

urlpatterns = [
    path('auth/register_client/', AuthRegisterClientView.as_view(), name='register_client'),
    re_path(r'^login/', LoginCustomView.as_view(), name='knox_custom_login'),
    re_path(r'^logout/', LogoutCustomView.as_view(), name='knox_logout'),
    re_path(r'^logoutall/', LogoutAllCustomView.as_view(), name='knox_logout_all')
]
