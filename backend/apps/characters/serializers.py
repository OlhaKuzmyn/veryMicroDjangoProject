from rest_framework.serializers import ModelSerializer

from .models import CharacterModel

# from apps.users.serializers import UserSerializer


class CharacterSerializer(ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = CharacterModel
        fields = (
            'id', 'name', 'race', 'dnd_beyond', 'char_class', 'user', 'createdAt', 'updatedAt'
        )
        read_only_fields = (
            'id', 'createdAt', 'updatedAt', 'user'
        )
