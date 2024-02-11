from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from clients.models import Clients

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home_view(request):
    data = Clients.objects.all()
    context = {"clients_table": data}
    return render(request, "home.html", context)
