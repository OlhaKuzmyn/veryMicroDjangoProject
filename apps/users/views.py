from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer

UserModel = get_user_model()


"""
    Create User
"""


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)


class UserListCreateView(ListCreateAPIView):  # ?
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)


# class UserRetrieveUpdateDestroyView(GenericAPIView):
#     serializer_class = UserSerializer
#     queryset = UserModel.objects.all()
#     permission_classes = (IsAuthenticated,)
#     lookup_field = None
#
#     def get(self, *args, **kwargs):
#         email = self.request.user
#         # queryset = UserModel.objects.filter(email=email)
#         # print(queryset)
#         return Response(UserSerializer(email).data)
#
#     def patch(self, pk=None, *args, **kwargs):
#         email = self.request.user
#         user = self.get_object()
#         print(user)
#         queryset = UserModel.objects.filter(email=email)
#         print(queryset)
#         return Response('patch')
