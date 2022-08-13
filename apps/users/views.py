from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer

UserModel = get_user_model()


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
