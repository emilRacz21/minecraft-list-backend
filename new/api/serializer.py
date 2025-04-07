from rest_framework import serializers
from .models import MinecraftServer, User, Login, ServerType, ServerVersion

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

class MinecraftServerSerializer(serializers.ModelSerializer):
        server_type = ServerTypeSerializer(many=True, read_only=True)
        server_version = ServerVersionSerializer(many=True, read_only=True)
        login = serializers.PrimaryKeyRelatedField(queryset=Login.objects.all())
        class Meta:
            model = MinecraftServer
            fields = '__all__'

class CheckServerSerializer(serializers.Serializer):
    ip = serializers.CharField()
    port = serializers.IntegerField(required=False, default=25565)
    login_id = serializers.IntegerField()