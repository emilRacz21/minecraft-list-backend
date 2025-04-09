# Generated by Django 5.0.14 on 2025-04-09 20:22

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256, unique=True)),
                ('password', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'mc_logins',
            },
        ),
        migrations.CreateModel(
            name='ServerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'mc_srv_types',
            },
        ),
        migrations.CreateModel(
            name='ServerVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'mc_srv_versions',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'mc_users',
            },
        ),
        migrations.CreateModel(
            name='MinecraftServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default='192.168.0.100', max_length=100)),
                ('port', models.IntegerField(blank=True, default=25565, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('publication_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('version', models.CharField(blank=True, max_length=100, null=True)),
                ('players_online', models.IntegerField(blank=True, null=True)),
                ('players_max', models.IntegerField(blank=True, null=True)),
                ('favicon', models.TextField(blank=True, null=True)),
                ('server_views', models.IntegerField(blank=True, default=1, null=True)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.login')),
                ('server_type', models.ManyToManyField(to='api.servertype')),
                ('server_version', models.ManyToManyField(to='api.serverversion')),
            ],
            options={
                'db_table': 'mc_servers_list',
            },
        ),
        migrations.CreateModel(
            name='ServerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=200)),
                ('created_at_date', models.DateField(default=datetime.date.today)),
                ('created_at_time', models.TimeField(auto_now_add=True)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.login')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.minecraftserver')),
            ],
            options={
                'db_table': 'mc_server_reviews',
            },
        ),
        migrations.AddField(
            model_name='login',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.CreateModel(
            name='LikedServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(choices=[(1, 'Like'), (-1, 'Dislike'), (0, 'No vote')], default=0)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.login')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.minecraftserver')),
            ],
            options={
                'db_table': 'mc_liked_servers',
                'unique_together': {('login', 'server')},
            },
        ),
    ]
