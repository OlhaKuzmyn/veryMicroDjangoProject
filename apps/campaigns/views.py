from datetime import datetime

from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.exceptions.campaign_over_exception import CampaignOverException
from core.exceptions.schedule_exception import ScheduleException
from core.permissions import IsDM, IsDMOrReadOnly

from apps.games.serializers import GameSerializer

from .filters import CampaignFilter
from .models import CampaignModel
from .serializers import CampaignSerializer

"""
    Create campaign
    Get Campaigns
"""


class CampaignListCreateView(ListCreateAPIView):
    serializer_class = CampaignSerializer
    queryset = CampaignModel.objects.all()
    # permission_classes = (IsAuthenticated & IsDMOrReadOnly)
    permission_classes = (IsDMOrReadOnly,)
    filterset_class = CampaignFilter

    # def get_queryset(self):
    #     self.queryset.filter(start_scheduledAt__year=)
    # def get_queryset(self):
    #     self.queryset.filter(title__)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(dms=[user])


"""
    Get only filtered campaigns
"""


class CampaignFilteredView(ListAPIView):  # return and change?
    serializer_class = CampaignSerializer
    queryset = CampaignModel.objects.all()
    permission_classes = (IsDMOrReadOnly,)

    def get_queryset(self):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        return CampaignModel.objects.filter(start_scheduledAt__year=year, start_scheduledAt__month=month)


"""
    Get, Update, Delete campaign
"""


class CampaignRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CampaignSerializer
    queryset = CampaignModel.objects.all()
    permission_classes = (IsDMOrReadOnly,)


"""
    Create Game
    Adds Game to a campaign
"""


class AddGameToCampaign(CreateAPIView):
    queryset = CampaignModel
    serializer_class = GameSerializer
    permission_classes = (IsDM,)

    def perform_create(self, serializer):
        campaign = self.get_object()
        schedule = datetime.strptime(self.request.data.get('scheduledAt'), "%Y-%m-%d %H:%M").timestamp()
        user = self.request.user

        """
            Cannot add game to the campaign that's already over
        """

        if not campaign.is_ongoing:
            raise CampaignOverException

        """
            game cannot be scheduled before the campaign starts
        """

        if schedule < campaign.start_scheduledAt.timestamp():
            raise ScheduleException()

        serializer.save(dm=user, campaign=campaign)
