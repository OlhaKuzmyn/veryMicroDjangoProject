from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from core.permissions import IsDM, IsDMOrReadOnly

from .models import GameModel
from .serializers import CampaignFieldSerializer, GameSerializer


class GameCreateListView(ListCreateAPIView):
    serializer_class = GameSerializer
    queryset = GameModel.objects.all()
    permission_classes = (IsDMOrReadOnly,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(dm=user)

    # def get_queryset(self):
    #     self.queryset.filter(scheduledAt__month='10')


class AddCampaign(GenericAPIView):
    # queryset = GameModel.objects.all()
    permission_classes = (IsDM,)

    def patch(self, *args, **kwargs):
        data = self.request.data
        serializer = CampaignFieldSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        print(data)
        return Response(data)
