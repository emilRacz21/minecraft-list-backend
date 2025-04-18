from django.db import models
import datetime

class User(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    class Meta:
        db_table = 'mc_users'

    def __str__(self):
        return f"{self.name} {self.lastname}"

class Login(models.Model):
    username = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256) 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'mc_logins'

    def __str__(self):
        return self.username

class ServerType(models.Model):
    name = models.CharField(max_length=100, unique=True)
  
    class Meta:
        db_table = 'mc_srv_types'

    def __str__(self):
        return self.name

class ServerVersion(models.Model):
    version = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'mc_srv_versions'

    def __str__(self):
        return self.version

class MinecraftServer(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    server_type = models.ManyToManyField(ServerType, blank=False)
    server_version = models.ManyToManyField(ServerVersion, blank=False)
    ip = models.CharField(max_length=100, default='192.168.0.100')
    port = models.IntegerField(null=True, blank=True, default=25565)
    description = models.CharField(max_length=500, null=True, blank=True)
    publication_date = models.DateField(default=datetime.date.today, null=True, blank=True) 
    update_date = models.DateField(auto_now=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    players_online = models.IntegerField(blank=True, null=True)
    players_max = models.IntegerField(blank=True, null=True)
    favicon = models.TextField(blank=True, null=True)
    server_views = models.IntegerField(default=1, blank=True, null=True)

    class Meta:
        db_table = 'mc_servers_list'

    def __str__(self):
        return f"{self.ip}:{self.port}"
    
class VoteChoices(models.IntegerChoices):
    LIKE = 1, 'Like'
    DISLIKE = -1, 'Dislike'
    NONE = 0, 'No vote'

class LikedServer(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    server = models.ForeignKey(MinecraftServer, on_delete=models.CASCADE)
    vote = models.IntegerField(choices=VoteChoices.choices, default=VoteChoices.NONE)

    class Meta:
        unique_together = ('login', 'server')
        db_table = 'mc_liked_servers'

    def __str__(self):
        return f"{self.login} -> {self.server} ({self.get_vote_display()})"
    
class ServerReview(models.Model):
    review = models.CharField(max_length=200)
    server = models.ForeignKey(MinecraftServer, on_delete=models.CASCADE)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    created_at_date = models.DateField(default=datetime.date.today)
    created_at_time = models.TimeField(auto_now_add=True)

    class Meta:
        db_table = 'mc_server_reviews'

    def __str__(self):
        return f"{self.login} on {self.server}: {self.review[:30]}..."