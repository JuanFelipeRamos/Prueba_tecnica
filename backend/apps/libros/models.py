from django.db import models
from autores.models import Autor
from bibliotecas.models import Biblioteca

class Libro(models.Model):
    title = models.CharField(max_length=60, verbose_name="Título")
    year_of_publication = models.IntegerField(verbose_name="Año de publicación")
    authors = models.ManyToManyField(Autor, verbose_name="Autor/es")
    libraries = models.ManyToManyField(Biblioteca, verbose_name="Bibliotecas")

    def __str__(self):
        return f"{self.title}"
