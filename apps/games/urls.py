from django.urls import path

from .views import GameCreateListView, GameFilteredView, GameRetrieveUpdateDestroyView

urlpatterns = [
    path('', GameCreateListView.as_view()),
    path('/<int:pk>', GameRetrieveUpdateDestroyView.as_view()),
    path('/<int:year>/<int:month>/filtered', GameFilteredView.as_view()),

]
