from django_filters import rest_framework as filters

from .models import ThreeDModel


class ThreeDModelFilter(filters.FilterSet):
    # Define a filter for start time and end time
    time_start = filters.DateTimeFilter(field_name='time_create', lookup_expr='gte')
    time_end = filters.DateTimeFilter(field_name='time_create', lookup_expr='lte')

    # Metaclass to provide metadata to the FilterSet
    class Meta:
        model = ThreeDModel
        fields = ['id', 'owner', 'time_create', 'time_update']
