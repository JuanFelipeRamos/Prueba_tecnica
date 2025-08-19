from django.db import models
from apps.autores.models import Autor
from apps.bibliotecas.models import Biblioteca

class Libro(models.Model):
    title = models.CharField(max_length=70, unique=True, verbose_name="Título")
    year_of_publication = models.IntegerField(verbose_name="Año de publicación")
    authors = models.ManyToManyField(Autor, verbose_name="Autor/es")
    libraries = models.ManyToManyField(Biblioteca, related_name="libros", verbose_name="Bibliotecas")

    def __str__(self):
        return f"{self.title}"
