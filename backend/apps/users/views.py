from django.contrib.auth import get_user_model

from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .serializers import ProfileSerializer, UserSerializer

UserModel = get_user_model()

"""
    Create User
"""


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)

    # def perform_create(self, serializer):
    #     prof = self.request.data.get('profile')
    #     serializer.save(display_name=" ".join([prof.get('name'), prof.get('surname')]))


"""
   Create User, get users as admin 
"""


class UserListCreateView(ListCreateAPIView):  # ?
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)


"""
    Update Profile
"""


class UpdateProfileView(UpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile


"""
    Get logged in User
"""


class GetUserView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserModel.objects.filter(id=self.request.user.id)
