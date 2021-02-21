from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import (
    ChangePassword,
    IndexView,
    LogoutView,
    SignUpView,
)

#app_name = ''
urlpatterns = [
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('user-change-password/', ChangePassword.as_view(), name='change-password'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', IndexView.as_view(), name='index'),
    url('^', include('django.contrib.auth.urls')),
]
