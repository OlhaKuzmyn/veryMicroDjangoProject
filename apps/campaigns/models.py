from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

from core.enums.validator_enums import ValidatorEnum

from apps.characters.models import CharacterModel

UserModel = get_user_model()


class CampaignModel(models.Model):
    class Meta:
        db_table = 'campaign'
        ordering = ['createdAt']

    dms = models.ManyToManyField(UserModel, related_name='campaigns')
    characters = models.ManyToManyField(CharacterModel, related_name='campaigns', default=None, blank=True)
    title = models.CharField(max_length=200, validators=[
        RegexValidator(
            ValidatorEnum.TITLE.pattern,
            ValidatorEnum.TITLE.msg
        )])
    description = models.TextField(max_length=3000, validators=[
        RegexValidator(
            ValidatorEnum.DESCRIPTION.pattern,
            ValidatorEnum.DESCRIPTION.msg
        )])
    start_scheduledAt = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
