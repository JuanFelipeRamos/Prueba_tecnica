from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BibliotecaViewSet

router = DefaultRouter()

router.register('bibliotecas', BibliotecaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
