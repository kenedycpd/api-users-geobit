
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from usuarios.views import UsersViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
