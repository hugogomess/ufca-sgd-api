from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.settings import api_settings

from .models import User
from .serializers import UserSerializer
from .filters import UserFilter
from .permissions import IsAdmin, IsAdminOrIsSelfUser

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdmin,)
    authentication_classes = (JSONWebTokenAuthentication,)
    filterset_class = UserFilter

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'partial_update':
            return [IsAuthenticated(), IsAdminOrIsSelfUser()]        
        return super(UserViewSet, self).get_permissions()

    # Override defalt destroy to soft delete
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        # Soft delete
        user.deleted_at = timezone.now()
        user.is_active = False
        user.save()

        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def activate(self, request, *args, **kwargs):
        user = self.get_object()
        # Active user
        user.is_active = True
        user.save()

        return Response(status=status.HTTP_200_OK)
