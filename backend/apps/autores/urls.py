from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet

router = DefaultRouter()

router.register('autores', AutorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
