from django.urls import path

from .views import AddGameToCampaign, CampaignListCreateView

urlpatterns = [
    path('', CampaignListCreateView.as_view()),
    path('/<int:pk>/game', AddGameToCampaign.as_view()),
]
