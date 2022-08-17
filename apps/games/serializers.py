from rest_framework.serializers import ModelSerializer

from .models import GameModel


class GameSerializer(ModelSerializer):
    class Meta:
        model = GameModel
        fields = (

        )