from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator, RegexValidator
from django.db import models

from core.enums.validator_enums import ValidatorEnum

UserModel = get_user_model()


class CharacterModel(models.Model):
    class Meta:
        db_table = 'character'

    name = models.CharField(max_length=300, validators=[
        MaxLengthValidator(300)
    ])
    race = models.CharField(max_length=200, validators=[
        MaxLengthValidator(200)
    ])
    dnd_beyond = models.URLField(max_length=300, blank=True, validators=[
        RegexValidator(
            ValidatorEnum.BEYOND_URL.pattern,
            ValidatorEnum.BEYOND_URL.msg
        )])
    char_class = models.CharField(max_length=200, validators=[
        MaxLengthValidator(200)
    ])  # Change to array with existing classes
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='characters')
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
