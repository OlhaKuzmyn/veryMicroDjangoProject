from rest_framework.serializers import ModelSerializer

from apps.characters.serializers import CharacterSerializer
from apps.users.serializers import UserSerializer

from .models import CampaignModel


class CampaignSerializer(ModelSerializer):
    dms = UserSerializer()
    characters = CharacterSerializer()

    class Meta:
        model = CampaignModel
        fields = (
            'id', 'dms', 'characters', 'title', 'description', 'start_scheduledAt', 'createdAt', 'updatedAt'
        )
        read_only_fields = (
            'id', 'dms', 'createdAt', 'updatedAt', 'characters'
        )
