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
from .views import MainModelCreateView # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.HomeView.as_view(), name='home'),          # Vista de inicio
    path('about/', main_views.AboutView.as_view(), name='about'),   # Vista "Acerca de"
    path('login/', user_views.LoginView.as_view(), name='login'), 
    path('crear/', MainModelCreateView.as_view(), name='mainmodel_create'),
    path('users/', include('users.urls')),
    path('', include('main.urls')),

]