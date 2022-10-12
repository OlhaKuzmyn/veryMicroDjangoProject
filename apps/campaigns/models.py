from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

from apps.characters.models import CharacterModel

UserModel = get_user_model()


class CampaignModel(models.Model):
    class Meta:
        db_table = 'campaign'
        ordering = ['createdAt']

    dms = models.ManyToManyField(UserModel, related_name='campaigns')
    characters = models.ManyToManyField(CharacterModel, related_name='campaigns', default=None, blank=True)
    title = models.CharField(max_length=300, validators=[
        MaxLengthValidator(300)
    ])
    description = models.TextField(max_length=3000, validators=[
        MaxLengthValidator(3000),
        MinLengthValidator(20)
    ])
    start_scheduledAt = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
