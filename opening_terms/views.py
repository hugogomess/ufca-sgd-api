from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from rest_framework.settings import api_settings

from .models import OpeningTerm
from .serializers import OpeningTermSerializer
from users.permissions import IsProjectManager
from .filters import OpeningTermFilter

class OpeningTermViewSet(ModelViewSet):
    queryset = OpeningTerm.objects.all()
    serializer_class = OpeningTermSerializer
    permission_classes = (IsAuthenticated, IsProjectManager,)
    authentication_classes = (JSONWebTokenAuthentication,)
    filterset_class = OpeningTermFilter

    # Override defalt destroy to method not allowed
    def destroy(self, request, *args, **kwargs):

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    