from django.urls import path

from .views import GameFilteredView, GameListView, GameRetrieveUpdateDestroyView

urlpatterns = [
    path('', GameListView.as_view()),
    path('/<int:pk>', GameRetrieveUpdateDestroyView.as_view()),
    path('/<int:year>/<int:month>/filtered', GameFilteredView.as_view()),

]
