from rest_framework import serializers
from django.utils import timezone

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
        error_messages={
            "blank": "Este campo é obrigatório.",
            "min_length": "A senha deve ter pelo menos 8 caracteres.",
        },
    )
    
    class Meta:
        model = User
        fields = ('id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'is_active',
            'is_admin',
            'is_project_manager',
            'is_demand_manager'
        )
        extra_kwargs = {
            'password': {'write_only':True},
            'is_active': {'read_only':True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


        