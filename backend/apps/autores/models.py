from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    nationality = models.CharField(max_length=100, verbose_name="Nacionalidad")

    def __str__(self):
        return f"{self.name}"
