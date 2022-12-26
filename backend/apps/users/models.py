from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxLengthValidator, RegexValidator
from django.db import models

from apps.users.managers import UserManager

from .enum import RegEx


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, validators=[
        RegexValidator(RegEx.PASSWORD.pattern, RegEx.PASSWORD.msg)
    ])
    is_dm = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    display_name = models.CharField(max_length=200, validators=[
        MaxLengthValidator(200)
    ])
    name = models.CharField(max_length=100, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    surname = models.CharField(max_length=100, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    tg_acc = models.CharField(max_length=100, validators=[RegexValidator(RegEx.TELEGRAM.pattern, RegEx.TELEGRAM.msg)])
    dc_acc = models.CharField(max_length=100, validators=[RegexValidator(RegEx.DISCORD.pattern, RegEx.DISCORD.msg)])
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')

