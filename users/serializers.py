from rest_framework.serializers import ModelSerializer
from django.utils import timezone
from django.contrib.auth.password_validation import validate_password

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
            'last_login',
            'password'
        )
        extra_kwargs = {'password': {'write_only':True}, 'is_active': {'read_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            validate_password(password)
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                validate_password(value)
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

        