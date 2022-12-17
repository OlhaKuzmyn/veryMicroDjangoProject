from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.exceptions.char_duplicate_exception import CharacterDuplicateException
from core.permissions import IsDM, IsDMOrReadOnly

from apps.characters.models import CharacterModel

from .filters import GameFilter
from .models import GameModel
from .serializers import GameSerializer

# from rest_framework.response import Response

"""
    Get games
"""


class GameListView(ListAPIView):
    serializer_class = GameSerializer
    queryset = GameModel.objects.all()
    permission_classes = (IsDMOrReadOnly,)
    filterset_class = GameFilter


"""
    Get only filtered games
"""


class GameFilteredView(ListAPIView):
    serializer_class = GameSerializer
    queryset = GameModel.objects.all()
    permission_classes = (IsDMOrReadOnly,)

    def get_queryset(self):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        return GameModel.objects.filter(scheduledAt__year=year, scheduledAt__month=month)


"""
    Get, update, delete a game
"""


class GameRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializer
    queryset = GameModel.objects.all()
    permission_classes = (IsDMOrReadOnly,)


"""
    Add character to a game
"""


class AddCharacterToGameView(GenericAPIView):
    queryset = GameModel.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated,)

    def patch(self, *args, **kwargs):
        char_id = self.request.data.get('char_id')
        game = self.get_object()
        new_character = get_object_or_404(CharacterModel, pk=char_id)
        """
            Character cannot be added twice
        """
        if game.characters.filter(pk=char_id).exists():
            raise CharacterDuplicateException
        game.characters.add(new_character)
        return Response(self.serializer_class(game).data)
