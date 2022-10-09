from django.urls import path

from .views import AddGameToCampaign, CampaignFilteredView, CampaignListCreateView

urlpatterns = [
    path('', CampaignListCreateView.as_view()),
    path('/<int:year>/<int:month>/filtered', CampaignFilteredView.as_view()),
    path('/<int:pk>/game', AddGameToCampaign.as_view()),
]
