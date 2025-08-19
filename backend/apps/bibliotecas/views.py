#pylint: disable=no-member
from rest_framework import viewsets, generics
from .models import Biblioteca
from .serializers import BibliotecaSerializer

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer


class BibliotecaUpdateView(generics.UpdateAPIView):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer
