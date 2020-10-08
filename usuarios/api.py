from django.shortcuts import redirect
from rest_framework import generics
from .models import Users
from .serializers import UsersSerializer


def home(request):
    return redirect('usuarios/api/create')


class UsersCreateApi(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersListApi(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersDeleteApi(generics.DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
