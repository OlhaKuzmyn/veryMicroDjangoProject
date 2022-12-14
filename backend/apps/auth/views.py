from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JwtService, RecoveryToken

from .serializers import EmailSerializer, ResetPasswordSerializer

UserModel = get_user_model()

"""
    Activate profile after creating user
"""


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        user = JwtService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


"""
    First step of resetting password 
"""


class CheckEmailView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # user = get_object_or_404(UserModel, email=serializer.data.get('email'))
        user = get_object_or_404(UserModel, email=data['email'])
        EmailService.reset_password(user)
        return Response(status.HTTP_200_OK)


"""
    Second step of resetting password 
    creating a new password
"""


class ResetPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = ResetPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = kwargs.get('token')
        user = JwtService.validate_token(token, RecoveryToken)
        # user.set_password(serializer.data.get('password'))
        user.set_password(data.get('password'))
        user.save()
        return Response(status.HTTP_200_OK)
