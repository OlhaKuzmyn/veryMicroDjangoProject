from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from core.permissions import IsDM, IsDMOrReadOnly

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
