from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Player
from .serializers import PlayerSerializer


class PlayerView(APIView):
    def get(self, request):
        players = Player.objects.all()
        player_serializer = PlayerSerializer(players,many=True)
        return Response(player_serializer.data)
