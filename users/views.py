from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.settings import api_settings

from .models import User
from .serializers import UserSerializer, UserSerializerCreate
from .filters import UserFilter

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filterset_class = UserFilter

    # Override create method
    def create(self, request, *args, **kwargs):

        self.serializer_class = UserSerializerCreate

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        try:
            headers =  {'Location': str(serializer.data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            headers = {}

        self.serializer_class = UserSerializer

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Override defalt destroy to soft delete
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        # Soft delete
        user.deleted_at = timezone.now()
        user.is_active = False
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def activate(self, request, *args, **kwargs):
        user = self.get_object()
        # Active user
        user.is_active = True
        user.save()

        return Response(status=status.HTTP_200_OK)
