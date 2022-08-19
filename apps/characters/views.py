from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import CharacterModel
from .serializers import CharacterSerializer


class CharacterListCreateView(ListCreateAPIView):
    serializer_class = CharacterSerializer
    queryset = CharacterModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
