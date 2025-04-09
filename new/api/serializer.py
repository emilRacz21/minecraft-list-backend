from rest_framework import serializers
from .models import MinecraftServer, User, Login, ServerType, ServerVersion, LikedServer, ServerReview

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
    login = serializers.PrimaryKeyRelatedField(queryset=Login.objects.all(), write_only=True)
    server = serializers.PrimaryKeyRelatedField(queryset=MinecraftServer.objects.all(), write_only=True)
    user_added = serializers.CharField(source='login.username', read_only=True)
    server_minecraft = serializers.CharField(source='server.ip', read_only=True)
    class Meta:
        model = LikedServer
        fields = ['id', 'user_added', 'server_minecraft', 'vote_display', 'vote', 'login', 'server']

class ServerReviewSerializer(serializers.ModelSerializer):
    login = serializers.PrimaryKeyRelatedField(queryset=Login.objects.all(), write_only=True)
    server = serializers.PrimaryKeyRelatedField(queryset=MinecraftServer.objects.all(), write_only=True)
    user_added = serializers.CharField(source='login.username', read_only=True)
    server_minecraft = serializers.CharField(source='server.ip', read_only=True)
    class Meta:
        model = ServerReview
        fields = ['id', 'review', 'server_minecraft', 'created_at_date', 'created_at_time', "user_added", 'login', 'server']

class MinecraftServerSerializer(serializers.ModelSerializer):
    server_type_name = ServerTypeSerializer(many=True, read_only=True, source='server_type')
    server_version_name = ServerVersionSerializer(many=True, read_only=True, source='server_version')
    login = serializers.PrimaryKeyRelatedField(queryset=Login.objects.all(), write_only=True)
    user_added = serializers.CharField(source='login.username', read_only=True)
    server_views = serializers.IntegerField(read_only=True)
    liked_votes = LikedServerSerializer(source='likedserver_set', many=True, read_only=True)
    server_reviews = ServerReviewSerializer(many=True, read_only=True,  source='serverreview_set')
    like_count = serializers.SerializerMethodField()
    dislike_count = serializers.SerializerMethodField()

    class Meta:
        model = MinecraftServer
        fields = [
            'id', 'server_type_name', 'server_version_name',
            'user_added', 'login', 'server_views', 'liked_votes',
            'server_reviews', 'ip', 'port', 'description', 
            'publication_date','update_date', 'version', 
            'players_online', 'players_max', 'favicon', 
            'like_count', 'dislike_count'  
            ]
        
    def get_like_count(self, obj):
        return obj.likedserver_set.filter(vote=1).count()

    def get_dislike_count(self, obj):
        return obj.likedserver_set.filter(vote=-1).count()
    

class CheckServerSerializer(serializers.Serializer):
    ip = serializers.CharField()
    port = serializers.IntegerField(required=False, default=25565)
    login_id = serializers.PrimaryKeyRelatedField(queryset=Login.objects.all())
    server_type = serializers.PrimaryKeyRelatedField(queryset=ServerType.objects.all(), required=True, many=True)
    server_version = serializers.PrimaryKeyRelatedField(queryset=ServerVersion.objects.all(), required=True, many=True)