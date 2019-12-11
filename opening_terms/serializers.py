from rest_framework import serializers
from .models import OpeningTerm
from demands.models import Demand

class OpeningTermSerializer(serializers.ModelSerializer):
    queryset = Demand.objects.all()
    demand = serializers.PrimaryKeyRelatedField(queryset=queryset)
    
    class Meta:
        model = OpeningTerm
        fields = (
            'id',
            'project_name',
            'demand',
            'opening_term',
            'created_at',
        )