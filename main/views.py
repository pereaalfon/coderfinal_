
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from .models import MainModel  
from .forms import MainModelForm 

@method_decorator(login_required, name='dispatch')
class MainModelCreateView(CreateView):
    model = MainModel
    form_class = MainModelForm  
    template_name = 'main/mainmodel_form.html'
    success_url = '/success/'  
from django.views.generic import ListView, DetailView, CreateView
from .models import Post  # Suponiendo que tienes un modelo Post para las publicaciones

class PostListView(ListView):
    model = Post
    template_name = 'main/post_list.html'  # Plantilla para listar las publicaciones
    context_object_name = 'posts'
    paginate_by = 5  # Número de publicaciones por página

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/post_detail.html'  # Plantilla para ver una publicación individual
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'main/post_form.html'  # Plantilla para crear una nueva publicación
    fields = ['title', 'content']  # Campos del formulario
    success_url = '/'  # Redirige a la lista de publicaciones después de crear
