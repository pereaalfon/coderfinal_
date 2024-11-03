from django.urls import path
from .views import MessageCreateView

urlpatterns = [
    path('new/', MessageCreateView.as_view(), name='message_create'),  # Ruta para crear un mensaje
]
