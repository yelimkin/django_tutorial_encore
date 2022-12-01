from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreateUserForm

class UserCreateView(CreateView):
    pass

class UserCreateDoneTV(TemplateView):
    pass