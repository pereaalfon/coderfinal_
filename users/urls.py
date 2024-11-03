
from django.urls import path
from .views import UserProfileView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user_profile'),  # Ruta para ver el perfil de usuario
]
