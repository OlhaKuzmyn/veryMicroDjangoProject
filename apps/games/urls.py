from django.urls import path

from .views import AddCampaign, GameCreateListView

urlpatterns = [
    path('', GameCreateListView.as_view()),
    path('/campaign', AddCampaign.as_view()),
]
