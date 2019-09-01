from rest_framework.serializers import ModelSerializer
from django.utils import timezone

from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'last_login'
        )

class UserSerializerCreate(ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        )
        