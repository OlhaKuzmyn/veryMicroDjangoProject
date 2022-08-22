from django.urls import path

from .views import GameCreateListView

urlpatterns = [
    path('', GameCreateListView.as_view()),
    # path('/<int:pk>/campaign', AddCampaign.as_view()),
]
