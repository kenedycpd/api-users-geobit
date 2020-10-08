from django.contrib import admin
from django.urls import include, path
from usuarios import api

urlpatterns = [
    path('', api.home, name='home'),
    path('usuarios/', include('usuarios.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
