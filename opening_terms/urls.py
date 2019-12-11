from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'opening-term', views.OpeningTermViewSet)

urlpatterns = [
    path('', include(router.urls))
]
