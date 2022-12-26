from django.urls import path

from .views import CharacterListCreateView, CharacterRetrieveUpdateDestroyView

urlpatterns = [
    path('', CharacterListCreateView.as_view()),
    path('/<int:pk>', CharacterRetrieveUpdateDestroyView.as_view()),

]