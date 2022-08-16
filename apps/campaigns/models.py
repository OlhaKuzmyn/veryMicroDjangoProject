from django.contrib.auth import get_user_model
from django.db import models

from apps.characters.models import CharacterModel
from apps.games.models import GameModel

UserModel = get_user_model()


class CampaignModel(models.Model):
    class Meta:
        db_table = 'campaign'
        ordering = ['createdAt']

    dms = models.ManyToManyField(UserModel, related_name='campaigns')
    characters = models.ManyToManyField(CharacterModel, related_name='campaigns')
    games = models.ManyToManyField(GameModel, related_name='games')
    title = models.CharField(max_length=200, validators=[])
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
