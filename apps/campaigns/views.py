from rest_framework.generics import ListCreateAPIView

from core.permissions import IsDMOrReadOnly

from .models import CampaignModel
from .serializers import CampaignSerializer


class CampaignListCreateView(ListCreateAPIView):
    serializer_class = CampaignSerializer
    queryset = CampaignModel.objects.all()
    permission_classes = (IsDMOrReadOnly,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(dms=[user])
