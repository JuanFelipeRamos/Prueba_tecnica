from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from django.conf import settings
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "password"]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

        def create(self, validated_data):
            clave_acceso = validated_data.get('key_admin')

            if clave_acceso != settings.KEY_ACCESS_ADMIN:
                return Response ({
                    'error': 'error al crear usuario admin, la clave de acceso ingresada es errónea.'
                }, status=status.HTTP_400_BAD_REQUEST)

            password = validated_data.pop('password')
            user = Usuario(**validated_data)
            user.set_password(password)
            user.is_superuser = True
            user.save()

            return user

class EditUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["first_name", "last_name"]
