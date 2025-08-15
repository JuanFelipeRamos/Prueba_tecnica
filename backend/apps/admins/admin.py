from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    # Campos que se mostrarán en la lista de usuarios
    list_display = (
        "username",
        "first_name",
        "is_staff",
        "is_active",
    )

    # Campos por los que se puede filtrar
    list_filter = ("is_staff", "is_active")

    # Campos que se pueden buscar
    search_fields = ("username", "first_name")

    # Ordenamiento por defecto
    ordering = ("username",)

    # Campos que se mostrarán en el formulario de edición
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Información Personal",
            {"fields": ("first_name", "last_name")},
        ),
        (
            "Permisos",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Fechas importantes", {"fields": ("last_login", "date_joined")}),
    )

    # Campos que se mostrarán en el formulario de creación
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

admin.site.register(Usuario, UsuarioAdmin)
