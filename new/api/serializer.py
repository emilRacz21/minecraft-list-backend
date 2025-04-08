from rest_framework import serializers
from .models import MinecraftServer, User, Login, ServerType, ServerVersion, LikedServer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

class ServerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerType
        fields = '__all__'

class ServerVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerVersion
        fields = '__all__'


class LikedServerSerializer(serializers.ModelSerializer):
    vote_display = serializers.CharField(source='get_vote_display', read_only=True)

    class Meta:
        model = LikedServer
        fields = ['id', 'login', 'server', 'vote', 'vote_display']


class MinecraftServerSerializer(serializers.ModelSerializer):
    server_type_name = ServerTypeSerializer(many=True, read_only=True, source='server_type')
    server_version_name = ServerVersionSerializer(many=True, read_only=True, source='server_version')
    login = serializers.PrimaryKeyRelatedField(queryset=Login.objects.all())
    server_views = serializers.IntegerField(read_only=True)
    user_added = serializers.CharField(source='login.username', read_only=True) 
    liked_votes = LikedServerSerializer(source='likedserver_set', many=True, read_only=True)

    class Meta:
        model = MinecraftServer
        fields = [
            'id', 'server_type_name', 'server_version_name',
            'login', 'server_views', 'user_added', 'liked_votes',
            'ip', 'port', 'description', 'publication_date',
            'update_date', 'version', 'players_online', 
            'players_max', 'favicon'  
            ]

class CheckServerSerializer(serializers.Serializer):
    ip = serializers.CharField()
    port = serializers.IntegerField(required=False, default=25565)
    login_id = serializers.PrimaryKeyRelatedField(queryset=Login.objects.all())
    server_type = serializers.PrimaryKeyRelatedField(queryset=ServerType.objects.all(), required=True, many=True)
    server_version = serializers.PrimaryKeyRelatedField(queryset=ServerVersion.objects.all(), required=True, many=True)