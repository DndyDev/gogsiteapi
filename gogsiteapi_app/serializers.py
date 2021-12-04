from rest_framework import serializers
from gogsiteapi_app.models import Player, Developer, Post


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'login', 'password', 'email', 'score', 'nickname')


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ('id', 'login', 'password', 'role')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'developer_id')
