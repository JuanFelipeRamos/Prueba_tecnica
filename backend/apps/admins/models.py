from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    """
    id
    username
    first_name
    last_name
    email
    password
    is_staff
    is_superuser
    date_joined
    last_login
    etc.
    """

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.username} {self.first_name}"

    class Meta:
        verbose_name = 'Usuario administrador'
        verbose_name_plural = 'Usuarios administradores'
