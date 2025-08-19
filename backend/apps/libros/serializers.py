#pylint: disable=no-member
from rest_framework import serializers
from apps.autores.serializers import AutorSerializer
from apps.bibliotecas.serializers import BibliotecaSerializer
from apps.autores.models import Autor
from apps.bibliotecas.models import Biblioteca
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):
    authors = AutorSerializer(many=True, read_only=True)
    libraries = BibliotecaSerializer(many=True, read_only=True)

    authors_ids = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all(), many=True, write_only=True
    )
    libraries_ids = serializers.PrimaryKeyRelatedField(
        queryset=Biblioteca.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Libro
        fields = [
            'id', 'title', 'year_of_publication',
            'authors', 'libraries',
            'authors_ids', 'libraries_ids'
        ]

    def create(self, validated_data):
        authors = validated_data.pop('authors_ids', [])
        libraries = validated_data.pop('libraries_ids', [])
        libro = Libro.objects.create(**validated_data)
        libro.authors.set(authors)
        libro.libraries.set(libraries)
        return libro
