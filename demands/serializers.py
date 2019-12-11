from rest_framework import serializers
from .models import Demand
from gut_matrices.models import GutMatrix

class DemandSerializer(serializers.ModelSerializer):
    queryset = GutMatrix.objects.all()
    gut_matrix = serializers.PrimaryKeyRelatedField(read_only=False, queryset=queryset, allow_null=True, default=None)

    class Meta:
        model = Demand
        fields = (
            'id',
            'name',
            'description',
            'requester',
            'requester_email',
            'origin',
            'status',
            'gut_matrix',
            'created_at'
        )