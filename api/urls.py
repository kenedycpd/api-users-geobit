from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
from django.urls import include, path
from usuarios import api

urlpatterns = [
    path('', api.home, name='home'),
    path('usuarios/', include('usuarios.urls')),
    path('usuarios/', obtain_jwt_token),
    path('admin/', admin.site.urls),
]
