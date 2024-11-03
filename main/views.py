from django.shortcuts import render

from django.views.generic import ListView
from .models import MainModel

class MainModelListView(ListView):
    model = MainModel
    template_name = 'main/home.html'
    context_object_name = 'objects'
    paginate_by = 10  
    
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
