from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User  # Suponiendo que usas el modelo de usuario de Django

class UserProfileView(View):
    def get(self, request):
        # Obtén el perfil del usuario actual (asumiendo que el usuario está autenticado)
        user = request.user
        return render(request, 'users/profile.html', {'user': user})
