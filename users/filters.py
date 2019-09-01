import django_filters
from django_filters import rest_framework as filters
from .models import User

class UserFilter(django_filters.FilterSet):
    # lookup_expr = 'startswith', 'endswith', 'contains', 'istartswith', 'iendswith',
    # 'icontains', 'exact', 'iexact'
   username = filters.CharFilter(field_name="username", lookup_expr='startswith')
   email = filters.CharFilter(field_name="email", lookup_expr='startswith')
   first_name = filters.CharFilter(field_name="first_name", lookup_expr='contains')
   last_name = filters.CharFilter(field_name="last_name", lookup_expr='contains')
   