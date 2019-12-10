from rest_framework import serializers
from .models import GutMatrix

class GutMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = GutMatrix
        fields = (
            'id',
            'name',
            'gravity',
            'urgency',
            'trend',
            'gut',
            'created_at',
        )