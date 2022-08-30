from django_filters import rest_framework as filters

from .models import CampaignModel


class CampaignFilter(filters.FilterSet):
    campaign_month = filters.DateTimeFilter(field_name='start_scheduledAt', lookup_expr='__year')

    class Meta:
        model = CampaignModel
        fields = ('campaign_month',)
