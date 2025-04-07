from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginViewSet, ServerTypeViewSet, ServerVersionViewSet, MinecraftServerViewSet, CheckAndAddMinecraftServer

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'logins', LoginViewSet)
router.register(r'server-types', ServerTypeViewSet)
router.register(r'server-versions', ServerVersionViewSet)
router.register(r'minecraft-servers', MinecraftServerViewSet)
router.register(r'check-server', CheckAndAddMinecraftServer, basename='check-server')



urlpatterns = [
    path('', include(router.urls))
]
