from typing import Type

from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.serializers import ModelSerializer, ValidationError

from core.services.email_service import EmailService

from apps.characters.serializers import CharacterSerializer

from .models import ProfileModel, UserModel

UserModel: Type[UserModel] = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        exclude = ('user',)

    def create(self, validated_data):
        print(validated_data)



class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()
    characters = CharacterSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_dm', 'last_login', 'is_superuser',
            'is_staff', 'is_active', 'profile', 'created_at', 'updated_at', 'characters'
        )
        read_only_fields = (
            'id', 'is_staff', 'is_active', 'last_login',
            'is_superuser', 'created_at', 'updated_at', 'profile', 'characters'
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        print(validated_data)

    def update(self, instance, validated_data):
        print(validated_data)

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']
        if email == password:
            raise ValidationError({'email_eq_password': 'email equal password'})
        return attrs

    @transaction.atomic  # when 2 models are used
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        EmailService.register_email(user)
        return user
