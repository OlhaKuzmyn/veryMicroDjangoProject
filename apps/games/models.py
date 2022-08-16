from django.contrib.auth import get_user_model
from django.db import models

from apps.characters.models import CharacterModel

UserModel = get_user_model()


class GameModel(models.Model):
    class Meta:
        db_table = 'game'
        ordering = ['createdAt']

    dm_id = models.ManyToManyField(UserModel, related_name='games')
    title = models.CharField(max_length=200, validators=[])
    description = models.TextField(max_length=3000)
    characters = models.ManyToManyField(CharacterModel, related_name='games')
    game_type = models.CharField(max_length=300, validators=[])  # not required
    scheduledAt = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
