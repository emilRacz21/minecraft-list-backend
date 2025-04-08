from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginViewSet, ServerTypeViewSet, ServerVersionViewSet, CheckAndAddMinecraftServer, LikedServerViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'logins', LoginViewSet)
router.register(r'server-types', ServerTypeViewSet)
router.register(r'server-versions', ServerVersionViewSet)
router.register(r'liked-server', LikedServerViewSet)
router.register(r'minecraft-server', CheckAndAddMinecraftServer, basename='check-server')

urlpatterns = [
    path('', include(router.urls))
]
