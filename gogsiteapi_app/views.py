from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Player, Developer, Post
from .serializers import PlayerSerializer, DeveloperSerializer, PostSerializer


class PlayerList(APIView):
    def get(self, request):
        players = Player.objects.all()
        player_serializer = PlayerSerializer(players, many=True)
        return Response(player_serializer.data)

    def post(self, request):
        player_serializer = PlayerSerializer(data=request.data)
        if player_serializer.is_valid():
            player_serializer.save()
            return Response(player_serializer.data)


class PlayerDetail(APIView):
    def get(self, request, pk):
        try:
            player = Player.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        player_serializer = PlayerSerializer(instance=player)
        return Response(player_serializer.data)

    def put(self, request, pk):
        try:
            player = Player.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        player_serializer = PlayerSerializer(instance=player, data=request.data, partial=True)
        if player_serializer.is_valid():
            player_serializer.save()
        return Response(player_serializer.data)

    def delete(self, request, pk):
        try:
            player = Player.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        player_serializer = PlayerSerializer(instance=player)
        player.delete()
        return Response(player_serializer.data)


class DeveloperList(APIView):
    def get(self, request):
        developers = Developer.objects.all();
        developer_serializer = DeveloperSerializer(developers, many=True)
        return Response(developer_serializer.data)

    def post(self, request):
        developer_serializer = DeveloperSerializer(data=request.data)
        if developer_serializer.is_valid():
            developer_serializer.save()
            return Response(developer_serializer.data)


class DeveloperDetail(APIView):
    def get(self, request, pk):
        try:
            developer = Developer.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        developer_serializer = DeveloperSerializer(instance=developer)
        return Response(developer_serializer.data)

    def put(self, request, pk):
        try:
            developer = Developer.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        developer_serializer = DeveloperSerializer(instance=developer, data=request.data, partial=True)
        if developer_serializer.is_valid():
            developer_serializer.save()
        return Response(developer_serializer.data)

    def delete(self, request, pk):
        try:
            developer = Developer.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        developer_serializer = DeveloperSerializer(instance=developer)
        developer.delete()
        return Response(developer_serializer.data)


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        post_serializer = PostSerializer(posts, many=True)
        return Response(post_serializer.data)

    def post(self, request):
        posts = Post.objects.all()
        post_setializer = PostSerializer(posts, many=True)
        if post_setializer.is_valid():
            post_setializer.save()
        return Response(post_setializer.data)


class PostDetail(APIView):

    def get(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post_serializer = PostSerializer(instance=post)
        return Response(post_serializer.data)

    def put(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post_serializer = PostSerializer(instance=post, data=request.data, partial=True)
        if post_serializer.is_valid():
            post_serializer.save()
        return Response(post_serializer.data)

    def delete(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post_serializer = PostSerializer(instance=post)
        post.delete()
        return Response(post_serializer.data)

    # ToDo: Проверить работу функции

    # def is_exist(self, in_object, in_model, pk):
    #     try:
    #         in_object = in_model.objects.get(id=pk)
    #     except ObjectDoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     return in_object
