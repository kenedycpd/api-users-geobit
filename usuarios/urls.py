from django.urls import path
from .api import *

urlpatterns = [
    path('api/list', UsersListApi.as_view()),
    path('api/create', UsersCreateApi.as_view()),
    path('api/<int:pk>/', UsersUpdateApi.as_view()),
    path('api/<int:pk>/delete', UsersDeleteApi.as_view()),
]
