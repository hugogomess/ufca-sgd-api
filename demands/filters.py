import django_filters
from django_filters import rest_framework as filters
from .models import Demand

class DemandFilter(django_filters.FilterSet):
    # lookup_expr = 'startswith', 'endswith', 'contains', 'istartswith', 'iendswith',
    # 'icontains', 'exact', 'iexact'
   name = filters.CharFilter(field_name="name", lookup_expr='contains')
   description = filters.CharFilter(field_name="description", lookup_expr='contains')
   requester = filters.CharFilter(field_name="requester", lookup_expr='contains')
   requester_email = filters.CharFilter(field_name="requester_email", lookup_expr='contains')
   origin = filters.CharFilter(field_name="origin", lookup_expr='contains')
   status = filters.CharFilter(field_name="status", lookup_expr='exact')

   