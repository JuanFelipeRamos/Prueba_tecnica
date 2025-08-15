from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Usuario
from .serializers import UsuarioSerializer, EditUsuarioSerializer

# vista para crear superusuarios
class RegistroUsuarioView(CreateAPIView):
    queryset = Usuario
    serializer_class = UsuarioSerializer


# vista para actualizar superusuarios
class EditUsuarioView(RetrieveUpdateAPIView):
    serializer_class = EditUsuarioSerializer
    permission_classes = [IsAuthenticated]
