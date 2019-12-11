import django_filters
from django_filters import rest_framework as filters
from .models import GutMatrix

class GutMatrixFilter(django_filters.FilterSet):
    # lookup_expr = 'startswith', 'endswith', 'contains', 'istartswith', 'iendswith',
    # 'icontains', 'exact', 'iexact'
   name = filters.CharFilter(field_name="name", lookup_expr='contains')

   