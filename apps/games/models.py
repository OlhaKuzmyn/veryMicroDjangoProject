from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from django.db import models

from core.enums.validator_enums import ValidatorEnum

from apps.campaigns.models import CampaignModel
from apps.characters.models import CharacterModel

UserModel = get_user_model()


class GameModel(models.Model):
    class Meta:
        db_table = 'game'
        ordering = ['createdAt']

    dm = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='games')
    title = models.CharField(max_length=300, validators=[
        MaxLengthValidator(300)
    ])
    description = models.TextField(max_length=3000, blank=True, validators=[
        MaxLengthValidator(3000),
        MinLengthValidator(20)
    ])
    characters = models.ManyToManyField(CharacterModel, related_name='games', blank=True)
    game_type = models.CharField(max_length=300, blank=True, validators=[
        MaxLengthValidator(300)
    ])
    campaign = models.ForeignKey(CampaignModel, on_delete=models.CASCADE, related_name='games')
    scheduledAt = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
