from django.urls import path

from .views import CharacterListCreateView

urlpatterns = [
    path('', CharacterListCreateView.as_view())
]