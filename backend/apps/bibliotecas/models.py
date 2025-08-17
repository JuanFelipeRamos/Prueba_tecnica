from django.db import models

class Biblioteca(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    location = models.CharField(max_length=40, blank=True, null=True, verbose_name='Ubicación')
    type_choises = {
        'virtual': 'virtual',
        'fisica': 'fisica'
    }
    type_biblioteca = models.CharField(max_length=10, choices=type_choises, default='virtual', verbose_name='tipo de biblioteca')


    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Biblioteca'
        verbose_name_plural = 'Bibliotecas'
