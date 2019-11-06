from rest_framework import serializers
from .models import Demand

class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = (
            'id',
            'name',
            'description',
            'requester',
            'origin',
            'status',
            'created_at'
        )