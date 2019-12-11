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
from .permissions import IsAdmin

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdmin,)
    authentication_classes = (JSONWebTokenAuthentication,)
    filterset_class = UserFilter

    # Override defalt destroy to soft delete
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        logged_user_id = None
        
        if request.user.is_authenticated:
            logged_user_id = request.user.id

        if logged_user_id == user.id:
            error_message = {
                "user": [
                    "Você não pode excluír seu próprio usuário!"
                ]
            }

            return Response(status=status.HTTP_400_BAD_REQUEST, data=error_message)
        else:
            try:
                # Soft delete
                user.deleted_at = timezone.now()
                user.is_active = False
                user.save()

                return Response(status=status.HTTP_200_OK)
            except Exception:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['get'])
    def activate(self, request, *args, **kwargs):
        user = self.get_object()
        
        try:
            # Active user
            user.is_active = True
            user.save()

            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
