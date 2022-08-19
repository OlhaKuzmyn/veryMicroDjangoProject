from rest_framework.serializers import ModelSerializer

from apps.users.serializers import UserSerializer

from .models import CharacterModel


class CharacterSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CharacterModel
        fields = (
            'id', 'name', 'race', 'dnd_beyond', 'char_class', 'user', 'createdAt', 'updatedAt'
        )
        read_only_fields = (
            'id', 'createdAt', 'updatedAt', 'user'
        )
