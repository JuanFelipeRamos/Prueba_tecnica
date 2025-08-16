from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Usuario
from .serializers import UsuarioSerializer, EditUsuarioSerializer

# vista para crear usuarios
class RegistroUsuarioView(CreateAPIView):
    queryset = Usuario
    serializer_class = UsuarioSerializer


# vista para actualizar usuarios
class EditUsuarioView(RetrieveUpdateAPIView):
    serializer_class = EditUsuarioSerializer
    permission_classes = [IsAuthenticated]
