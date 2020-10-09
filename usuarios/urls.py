from django.urls import path
from .api import *

urlpatterns = [
    path('api/list', CustomUserListApi.as_view()),
    path('api/create', CustomUserCreateApi.as_view()),
    path('api/<int:pk>/', CustomUserUpdateApi.as_view()),
    path('api/<int:pk>/delete', CustomUserDeleteApi.as_view()),
]
