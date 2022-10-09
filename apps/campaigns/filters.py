from django_filters import rest_framework as filters

from .models import CampaignModel


class CampaignFilter(filters.FilterSet):
    campaign_day = filters.NumberFilter(field_name='start_scheduledAt', lookup_expr='day')
    campaign_month = filters.NumberFilter(field_name='start_scheduledAt', lookup_expr='month')
    campaign_year = filters.NumberFilter(field_name='start_scheduledAt', lookup_expr='year')

    class Meta:
        model = CampaignModel
        fields = ('campaign_day', 'campaign_month', 'campaign_year')
