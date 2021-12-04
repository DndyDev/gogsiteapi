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

    #ToDo: Проверить работу функции

    # def is_exist(self, in_object, in_model, pk):
    #     try:
    #         in_object = in_model.objects.get(id=pk)
    #     except ObjectDoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     return in_object
