from django.urls import path
from .api import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
urlpatterns = [
    path('api/list', CustomUserListApi.as_view()),
    path('api/create', CustomUserCreateApi.as_view()),
    path('api/<int:pk>/', CustomUserUpdateApi.as_view()),
    path('api/<int:pk>/delete', CustomUserDeleteApi.as_view()),
    path('api/token', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
]
