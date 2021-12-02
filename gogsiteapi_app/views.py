from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Player


class PlayerView(APIView):
    def get(self):
        players = Player.objects.all();
        return Response({"players": players})
