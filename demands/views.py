from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from rest_framework.settings import api_settings
from django.db.models import Count
from rest_framework.decorators import action
from django.core.mail import send_mail
from django.conf import settings

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

    @action(detail=True, methods=['post'], url_path='switch-status')
    def switch_status(self, request, *args, **kwargs):
        demand = self.get_object()        
        demand_status = request.POST.get['status']

        if demand_status != 'ABERTA' and demand_status != 'EM ANDAMENTO' and demand_status != 'FECHADA':
            error_message = {
                "status": [
                    "'" + demand_status + "' não é um escolha válida."
                ]
            }

            return Response(status=status.HTTP_400_BAD_REQUEST, data=error_message)

        elif demand_status == demand.status:
            error_message = {
                "status": [
                    "A demanda já está com o status '" + demand_status + "'."
                ]
            }

            return Response(status=status.HTTP_400_BAD_REQUEST, data=error_message)
        else:
            try:
                demand.status = demand_status
                demand.save()

                subject = "O status da demanda '" + demand.name + "' foi atualizado!"
                message = "Olá " + demand.requester + ", a demanda '" + demand.name + "' que você solicitou teve seu status atualizado para '" + demand.status + "'."
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [demand.requester_email,]
                send_mail( subject, message, email_from, recipient_list)

                return Response(status=status.HTTP_200_OK)
            except Exception:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    