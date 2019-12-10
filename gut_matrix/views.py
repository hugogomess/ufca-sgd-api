from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from rest_framework.settings import api_settings

from .models import GutMatrix
from .serializers import GutMatrixSerializer
from users.permissions import IsDemandManager
from .filters import GutMatrixFilter

class GutMatrixViewSet(ModelViewSet):
    queryset = GutMatrix.objects.all()
    serializer_class = GutMatrixSerializer
    permission_classes = (IsAuthenticated, IsDemandManager,)
    authentication_classes = (JSONWebTokenAuthentication,)
    filterset_class = GutMatrixFilter

    # Override defalt destroy to method not allowed
    def destroy(self, request, *args, **kwargs):

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    