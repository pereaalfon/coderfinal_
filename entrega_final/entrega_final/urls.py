"""
URL configuration for entrega_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from main import views as main_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.HomeView.as_view(), name='home'),          # Vista de inicio
    path('about/', main_views.AboutView.as_view(), name='about'),  # Vista "Acerca de"
    path('login/', user_views.LoginView.as_view(), name='login'),  # Vista de login
    path('crear/', main_views.MainModelCreateView.as_view(), name='mainmodel_create'),  # Vista de crear modelo en "main"
    
    # Incluye las URLs de las aplicaciones
    path('users/', include('users.urls')),  # URLs de la aplicación "users"
    path('main/', include('main.urls')),    # URLs de la aplicación "main" (evita usar '' para evitar conflicto)
]
