from django.urls import path

from .views import CampaignListCreateView

urlpatterns = [
    path('', CampaignListCreateView.as_view()),
]