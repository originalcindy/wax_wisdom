from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Index view for the blog
def index(request):
    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)

# About page view
def about_me(request):
    return HttpResponse("This would be the about page")

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import WorkshopBookingForm, ReviewForm
from .models import WorkshopBooking, Review, BlogPost

# Home Page
def index(request):
    return render(request, "index.html")

# About Page
def about_me(request):
    return render(request, "about.html")

# Register Page
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

# Login Page
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

# Logout Functionality
def user_logout(request):
    logout(request)
    return redirect("index")

# Book a Workshop
def book_workshop(request):
    if request.method == "POST":
        form = WorkshopBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = WorkshopBookingForm()
    return render(request, "book_workshop.html", {"form": form})

# Blog Section
def blog(request):
    posts = BlogPost.objects.all()
    return render(request, "blog.html", {"posts": posts})

# Leave a Review
def leave_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ReviewForm()
    return render(request, "leave_review.html", {"form": form})
