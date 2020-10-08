from django.shortcuts import redirect
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer


def home(request):
    return redirect('usuarios/api/create')


class CustomUserCreateApi(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserListApi(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDeleteApi(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
