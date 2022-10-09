from django_filters import rest_framework as filters

from .models import GameModel


class GameFilter(filters.FilterSet):
    game_day = filters.NumberFilter(field_name='scheduledAt', lookup_expr='day')
    game_month = filters.NumberFilter(field_name='scheduledAt', lookup_expr='month')
    game_year = filters.NumberFilter(field_name='scheduledAt', lookup_expr='year')

    class Meta:
        model = GameModel
        fields = ('game_day', 'game_month', 'game_year')