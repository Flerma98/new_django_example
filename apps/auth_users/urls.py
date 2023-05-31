from django.urls import re_path
from knox.views import LogoutView, LogoutAllView

from apps.auth_users.views import LoginCustomView

urlpatterns = [
    re_path(r'^login/', LoginCustomView.as_view(), name='knox_custom_login'),
    re_path(r'^logout/', LogoutView.as_view(), name='knox_logout'),
    re_path(r'^logoutall/', LogoutAllView.as_view(), name='knox_logout_all'),
]
