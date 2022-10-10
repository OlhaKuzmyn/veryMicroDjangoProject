from django.urls import path

from .views import AddGameToCampaign, CampaignFilteredView, CampaignListCreateView, CampaignRetrieveUpdateDestroyView

urlpatterns = [
    path('', CampaignListCreateView.as_view()),
    path('/<int:pk>', CampaignRetrieveUpdateDestroyView.as_view()),
    path('/<int:year>/<int:month>/filtered', CampaignFilteredView.as_view()),
    path('/<int:pk>/game', AddGameToCampaign.as_view()),
]
