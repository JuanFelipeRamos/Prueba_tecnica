from rest_framework.generics import CreateAPIView
from .models import Usuario
from .serializers import UsuarioSerializer

# vista para crear usuarios
class RegistroUsuarioView(CreateAPIView):
    queryset = Usuario
    serializer_class = UsuarioSerializer
