from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('obtain-auth-token/', obtain_auth_token),
    path('', include(router.urls))
]
