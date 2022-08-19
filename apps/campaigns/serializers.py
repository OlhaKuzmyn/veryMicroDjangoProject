from rest_framework.serializers import ModelSerializer

from apps.characters.serializers import CharacterSerializer
from apps.games.serializers import GameSerializer
from apps.users.serializers import UserSerializer

from .models import CampaignModel


class CampaignSerializer(ModelSerializer):
    dms = UserSerializer(many=True, read_only=True)
    characters = CharacterSerializer(many=True, read_only=True)
    games = GameSerializer(many=True, read_only=True)

    class Meta:
        model = CampaignModel
        fields = (
            'id', 'dms', 'characters', 'title', 'games', 'description', 'start_scheduledAt', 'createdAt', 'updatedAt'
        )
        read_only_fields = (
            'id', 'dms', 'createdAt', 'updatedAt', 'characters'
        )
