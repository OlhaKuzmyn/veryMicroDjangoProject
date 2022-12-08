from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import CharacterModel
from .serializers import CharacterSerializer

"""
    Get current user characters
    create a new character for current user 
"""


class CharacterListCreateView(ListCreateAPIView):
    serializer_class = CharacterSerializer
    queryset = CharacterModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return CharacterModel.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


"""
    Get, update, delete character
"""


class CharacterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CharacterSerializer
    queryset = CharacterModel.objects.all()
    permission_classes = (IsAuthenticated,)
