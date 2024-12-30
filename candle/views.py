from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import LoginForm,SignUpForm


class HomeView(TemplateView):
    template_name = 'candle/home.html'

class CandleLoginView(LoginView):
    form_class = LoginForm
    template_name = "candle/login.html"
    # redirect_authenticated_user = True
    
class CandleSignUpView(CreateView):
    template_name = 'candle/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('candle:home')

    def form_valid(self, form):
        # Save the user first
        response = super().form_valid(form)
        # Log the user in
        login(self.request, self.object,backend="candle.backends.EmailOrUsernameModelBackend")
        messages.success(self.request, 'Account created successfully! Welcome aboard!')
        return response

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('candle:home')
        return super().get(request, *args, **kwargs)