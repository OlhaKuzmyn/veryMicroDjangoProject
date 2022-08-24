from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from core.permissions import IsDM, IsDMOrReadOnly

from .models import GameModel
from .serializers import GameSerializer

# class GameCreateListView(ListCreateAPIView):
#     serializer_class = GameSerializer
#     queryset = GameModel.objects.all()
#     permission_classes = (IsDMOrReadOnly,)
#
#     def perform_create(self, serializer):
#         user = self.request.user
#         data = self.request.data
#         serializer.save(dm=user, campaign_id=data['campaign_id'])
