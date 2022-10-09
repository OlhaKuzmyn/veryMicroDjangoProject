from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from core.permissions import IsDM, IsDMOrReadOnly

from .models import GameModel
from .serializers import GameSerializer


class GameCreateListView(ListAPIView):
    serializer_class = GameSerializer
    queryset = GameModel.objects.all()
    permission_classes = (IsDMOrReadOnly,)


class GameFilteredView(ListAPIView):
    serializer_class = GameSerializer
    queryset = GameModel.objects.all()
    permission_classes = (IsDMOrReadOnly,)

    def get_queryset(self):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        return GameModel.objects.filter(scheduledAt__year=year, scheduledAt__month=month)
