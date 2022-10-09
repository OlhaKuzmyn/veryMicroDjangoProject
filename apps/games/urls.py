from django.urls import path

from .views import GameCreateListView, GameFilteredView

urlpatterns = [
    path('', GameCreateListView.as_view()),
    path('/<int:year>/<int:month>/filtered', GameFilteredView.as_view()),

]
