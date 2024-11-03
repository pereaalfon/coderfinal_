from django.views.generic import CreateView
from .models import Message  # Suponiendo que tienes un modelo Message para los mensajes

class MessageCreateView(CreateView):
    model = Message
    template_name = 'messaging/message_form.html'  # Plantilla para crear un mensaje
    fields = ['content', 'post']  # Campos del formulario
    success_url = '/'  # Redirige a la lista de publicaciones después de enviar un mensaje
