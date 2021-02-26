"""djangoum2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'Blog Inexistente'  # Nome que aparece na tela de login e na barra do sistema
admin.site.site_title = 'Você cria posts mas não pode vê-los'  # Título que aparece na aba do navegador
admin.site.index_title = 'Gerenciamento de Posts'  # Título da página inicial da area administrativa
