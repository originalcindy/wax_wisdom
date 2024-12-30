from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from .forms import LoginForm

class HomeView(TemplateView):
    template_name = 'candle/home.html'

class CandleLoginView(LoginView):
    form_class = LoginForm
    template_name = "candle/login.html"
    # redirect_authenticated_user = True
    