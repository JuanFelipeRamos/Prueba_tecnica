from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/admins/', include('apps.admins.urls')),

    path('api/', include('apps.bibliotecas.urls')),
    path('api/', include('apps.autores.urls')),
    path('api/', include('apps.libros.urls')),
]
