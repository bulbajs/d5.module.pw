from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy


class CreateAccount(CreateView):
    form_class = SignUpForm
    model = User
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('/accounts/login')
