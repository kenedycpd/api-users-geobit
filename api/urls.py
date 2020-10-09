from django.contrib import admin
from django.urls import include, path
from usuarios import api
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
urlpatterns = [
    path('', api.home, name='home'),
    path('usuarios/', include('usuarios.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
