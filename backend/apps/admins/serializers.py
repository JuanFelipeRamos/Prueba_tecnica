from rest_framework import serializers
from django.conf import settings
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    key_admin = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "password", "key_admin"]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data.get('key_admin') != settings.KEY_ACCESS_ADMIN:
            raise serializers.ValidationError(
                {"error": "Error al crear usuario admin, la clave de acceso ingresada es errónea."}
            )
        return data

    def create(self, validated_data):
        validated_data.pop('key_admin', None)
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class EditUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["first_name", "last_name"]
