from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from rest_framework.settings import api_settings
from django.db.models import Count

from .models import Demand
from .serializers import DemandSerializer
from users.permissions import IsDemandManager
from .filters import DemandFilter

class DemandViewSet(ModelViewSet):
    queryset = Demand.objects.all().annotate(null_gut_matrix=Count('gut_matrix')).order_by('-null_gut_matrix', '-gut_matrix__gut' ,'-created_at')
    serializer_class = DemandSerializer
    permission_classes = (IsAuthenticated, IsDemandManager,)
    authentication_classes = (JSONWebTokenAuthentication,)
    filterset_class = DemandFilter

    # Override defalt destroy to method not allowed
    def destroy(self, request, *args, **kwargs):

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    