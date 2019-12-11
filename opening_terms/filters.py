import django_filters
from django_filters import rest_framework as filters
from .models import OpeningTerm

class OpeningTermFilter(django_filters.FilterSet):
    # lookup_expr = 'startswith', 'endswith', 'contains', 'istartswith', 'iendswith',
    # 'icontains', 'exact', 'iexact'
   project_name = filters.CharFilter(field_name="project_name", lookup_expr='contains')

   