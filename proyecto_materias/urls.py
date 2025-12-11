from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('materias.urls')),  # Importante: incluye las URLs de tu app
]