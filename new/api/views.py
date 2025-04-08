from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import MinecraftServer, User, Login, ServerType, ServerVersion, LikedServer
from .serializer import MinecraftServerSerializer, UserSerializer, LoginSerializer, ServerTypeSerializer, ServerVersionSerializer,CheckServerSerializer, LikedServerSerializer
from mcstatus.server import JavaServer 
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

class LikedServerViewSet(viewsets.ModelViewSet):
    queryset = LikedServer.objects.all()
    serializer_class = LikedServerSerializer
    permission_classes = [AllowAny]

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

        ip = serializer.validated_data["ip"].strip()
        port = serializer.validated_data.get("port", 25565)
        login_id = serializer.validated_data["login_id"]
        server_types = serializer.validated_data.get('server_type', [])
        server_versions = serializer.validated_data.get('server_version', [])

        if MinecraftServer.objects.filter(ip=ip, port=port).exists():
            return Response({"error": "Server with this IP and Port exist in our DB."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            server = JavaServer.lookup(f"{ip}:{port}")
            status_response = server.status()
        except Exception as e:
            return Response({"error": f"Can't connect to the server: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            login = Login.objects.get(pk=login_id.id)
        except Login.DoesNotExist:
            return Response({"error": "Your login ID not exist."}, status=status.HTTP_404_NOT_FOUND)

        mc_server, created = MinecraftServer.objects.get_or_create(
            login=login,
            ip=ip,
            port=port,
            defaults={
                "description": status_response.description or "No Description",
                "version": status_response.version.name,
                "players_online": status_response.players.online,
                "players_max": status_response.players.max,
                "favicon": status_response.favicon,
            }
        )

        mc_server.server_type.set(server_types)
        mc_server.server_version.set([version.id for version in server_versions])
        output_serializer = MinecraftServerSerializer(mc_server)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'], url_path='refresh-server')
    def check_server(self, request, pk=None):

        try:
            server = self.get_object()
        except MinecraftServer.DoesNotExist:
            return Response({"error": "Server not exist."}, status=status.HTTP_404_NOT_FOUND)
        try:
            java_server = JavaServer.lookup(f"{server.ip}:{server.port}")
            status_response = java_server.status()

            server.server_views += 1
            server.save(update_fields=['server_views'])

            server.players_online = status_response.players.online
            server.save(update_fields=['players_online'])
        except Exception as e:
            return Response({"error": f"Can't connect to the server: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(server)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='popular')
    def popular_servers(self, request):
        top_servers = MinecraftServer.objects.order_by('-players_online')[:10]
        serializer = self.get_serializer(top_servers, many=True)
        return Response(serializer.data)
