from rest_framework.generics import CreateAPIView, ListCreateAPIView

from core.permissions import IsDM, IsDMOrReadOnly

from apps.games.serializers import GameSerializer

from .models import CampaignModel
from .serializers import CampaignSerializer


class CampaignListCreateView(ListCreateAPIView):
    serializer_class = CampaignSerializer
    queryset = CampaignModel.objects.all()
    permission_classes = (IsDMOrReadOnly,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(dms=[user])


class AddGameToCampaign(CreateAPIView):
    queryset = CampaignModel
    serializer_class = GameSerializer
    permission_classes = (IsDM,)

    def perform_create(self, serializer):
        campaign = self.get_object()
        user = self.request.user
        serializer.save(dm=user, campaign=campaign)
