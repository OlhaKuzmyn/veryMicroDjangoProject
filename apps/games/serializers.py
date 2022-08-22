from rest_framework.serializers import ModelSerializer

from .models import GameModel


class GameSerializer(ModelSerializer):

    class Meta:
        model = GameModel
        fields = (
            'id', 'dm', 'title', 'description', 'characters',
            'game_type', 'scheduledAt', 'createdAt', 'updatedAt', 'campaign_id'
        )
        read_only_fields = (
            'id', 'createdAt', 'updatedAt', 'dm'
        )


class CampaignFieldSerializer(ModelSerializer):

    class Meta:
        model = GameModel
        fields = (
            'campaign',
        )
