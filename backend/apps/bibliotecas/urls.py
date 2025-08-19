from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BibliotecaViewSet, BibliotecaUpdateView

router = DefaultRouter()

router.register('bibliotecas', BibliotecaViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("editar/<int:pk>/", BibliotecaUpdateView.as_view(), name="editar-bibliotecas"),
]
