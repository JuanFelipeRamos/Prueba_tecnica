#pylint: disable=no-member
from rest_framework import serializers
from .models import Biblioteca

class RegistroBibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = ['name', 'location', 'type_biblioteca']

    def create(self, validated_data):
        tipo_bibl_ingresado = validated_data.get('type_biblioteca')

        if tipo_bibl_ingresado == 'Virtual':
            validated_data['location'] = ''
            return Biblioteca.objects.create(**validated_data)
        else:
            ubicacion_ingresada = validated_data.get('location')
            validated_data['location'] = ubicacion_ingresada
            return Biblioteca.objects.create(**validated_data)
