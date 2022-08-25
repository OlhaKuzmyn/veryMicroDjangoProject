from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response

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
        data = self.request.data
        campaign = self.get_object()
        user = self.request.user
        serializer.save(dm=user, campaign=campaign)

        # s = data.get('scheduledAt').split()[0].split('-')
        # if int(s[0]) >= campaign.start_scheduledAt.year:
        #     if int(s[1]) >= campaign.start_scheduledAt.month:
        #         if int(s[2]) >= campaign.start_scheduledAt.day:
        #             serializer.save(dm=user, campaign=campaign)
        # return Response('Game should be scheduled the same day or later than campaign starts',
        #                 status=status.HTTP_400_BAD_REQUEST)
