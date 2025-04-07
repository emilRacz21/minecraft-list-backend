from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import MinecraftServer, User, Login, ServerType, ServerVersion
from .serializer import MinecraftServerSerializer, UserSerializer, LoginSerializer, ServerTypeSerializer, ServerVersionSerializer,CheckServerSerializer
from mcstatus.server import JavaServer 
from .models import MinecraftServer, Login
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

class ServerTypeViewSet(viewsets.ModelViewSet):
    queryset = ServerType.objects.all()
    serializer_class = ServerTypeSerializer
    permission_classes = [AllowAny]

class ServerVersionViewSet(viewsets.ModelViewSet):
    queryset = ServerVersion.objects.all()
    serializer_class = ServerVersionSerializer
    permission_classes = [AllowAny]

class MinecraftServerViewSet(viewsets.ModelViewSet):
    queryset = MinecraftServer.objects.all()
    serializer_class = MinecraftServerSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.server_views = (instance.server_views or 0) + 1
        instance.save(update_fields=['server_views'])

        try:
            server = JavaServer.lookup(f"{instance.ip}:{instance.port}")
            status_response = server.status()
            instance.players_online = status_response.players.online
            instance.save(update_fields=['players_online'])
        except Exception as e:
            return Response({"error": f"Nie udało się połączyć z serwerem: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='popular')
    def popular_servers(self, request):
        top_servers = MinecraftServer.objects.order_by('-players_online')[:10]
        serializer = self.get_serializer(top_servers, many=True)
        return Response(serializer.data)
    
class CheckAndAddMinecraftServer(viewsets.ModelViewSet):
    queryset = MinecraftServer.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return CheckServerSerializer
        return MinecraftServerSerializer

    def create(self, request, *args, **kwargs):
        serializer = CheckServerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        ip = serializer.validated_data["ip"]
        port = serializer.validated_data.get("port", 25565)
        login_id = serializer.validated_data["login_id"]

        try:
            server = JavaServer.lookup(f"{ip}:{port}")
            status_response = server.status()
        except Exception as e:
            return Response({"error": f"Nie udało się połączyć z serwerem: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            login = Login.objects.get(pk=login_id)
        except Login.DoesNotExist:
            return Response({"error": "Nie znaleziono loginu o podanym ID."}, status=status.HTTP_404_NOT_FOUND)

        mc_server, created = MinecraftServer.objects.get_or_create(
            login=login,
            ip=ip,
            port=port,
            defaults={
                "description": status_response.description or "Brak opisu",
                "version": status_response.version.name,
                "players_online": status_response.players.online,
                "players_max": status_response.players.max,
                "favicon": status_response.favicon
            }
        )

        output_serializer = MinecraftServerSerializer(mc_server)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
