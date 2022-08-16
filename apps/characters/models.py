from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class CharacterModel(models.Model):
    class Meta:
        db_table = 'character'

    name = models.CharField(max_length=100, validators=[])
    race = models.CharField(max_length=100, validators=[])
    dnd_beyond = models.CharField(max_length=300, validators=[])  # not required
    char_class = models.CharField(max_length=100, validators=[])  # Change to array with existing classes
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='characters')
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
