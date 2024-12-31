from django.shortcuts import redirect,get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView,ListView,DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login

from .models import Blogpost,CandleWorkshop
from .forms import LoginForm,SignUpForm


class HomeView(TemplateView):
    template_name = 'candle/home.html'

class CandleLoginView(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = "candle/login.html"
    redirect_authenticated_user = True
    success_message = "Login Successful"
    
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
    
class CandleLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, "You have been logged out successfully.")
        return response
    
class AboutView(TemplateView):
    template_name = "candle/about.html"

class BlogListView(ListView):
    model = Blogpost
    template_name = 'candle/blogs.html'
    context_object_name = 'blogs'
    paginate_by = 10 

    
class WorkshopListView(ListView):
    model = CandleWorkshop
    template_name = 'candle/workshops.html'
    context_object_name = 'workshops'
    paginate_by = 10

class BlogDetail(DetailView):
    model = Blogpost
    template_name = 'candle/blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['related_blogs'] = Blogpost.objects.exclude(pk=self.object.pk).order_by('-published_date')[:2]
        
        return context
    
