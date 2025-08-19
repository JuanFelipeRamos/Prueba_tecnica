#pylint: disable=no-member
from rest_framework import serializers
from .models import Biblioteca

class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = ['id', 'name', 'location', 'type_biblioteca', 'libros']
        depth = 1

    def create(self, validated_data):
        tipo_bibl_ingresado = validated_data.get('type_biblioteca')

        if tipo_bibl_ingresado == 'virtual':
            validated_data['location'] = ''
            return Biblioteca.objects.create(**validated_data)
        else:
            ubicacion_ingresada = validated_data.get('location')
            validated_data['location'] = ubicacion_ingresada
            return Biblioteca.objects.create(**validated_data)
