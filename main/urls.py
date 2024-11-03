from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),  # Ruta para listar las publicaciones
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Ruta para ver una publicación
    path('post/new/', PostCreateView.as_view(), name='post_create'),  # Ruta para crear una nueva publicación
]
