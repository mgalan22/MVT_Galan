"""mvtGalan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from familia.views import ver_familia
from familia.views import crear_familia



urlpatterns = [
    path('admin/', admin.site.urls),
    path('ver/', ver_familia),      #muestra la lista de elementos de la BD
    path('crea/',crear_familia),  #agrega los 3 elementos de la vista a la BD y muestra confirmación
]
