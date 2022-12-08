from rest_framework.serializers import ModelSerializer

from ..characters.serializers import CharacterSerializer
from .models import GameModel


class GameSerializer(ModelSerializer):
    characters = CharacterSerializer(many=True, read_only=True)

    class Meta:
        model = GameModel
        fields = (
            'id', 'dm', 'title', 'description', 'characters',
            'game_type', 'scheduledAt', 'createdAt', 'updatedAt'
        )
        read_only_fields = (
            'id', 'createdAt', 'updatedAt', 'dm'
        )

