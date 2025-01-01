from django.shortcuts import redirect
from django.http import JsonResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView,ListView,DetailView,DeleteView
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError,PermissionDenied
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login
import json

from .models import Blogpost,CandleWorkshop,Booking,Review
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

class BookingCreateView(LoginRequiredMixin, View):
    http_method_names = ['post']
    
    def handle_no_permission(self):
        messages.error(self.request, 'Please login to book a workshop')
        return JsonResponse({
            'status': 'error',
            'message': 'Please login to book a workshop'
        }, status=403)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            workshop_id = data.get('workshopId')
            number_of_seats = data.get('seats')

            # validate input
            if not workshop_id or not number_of_seats:
                messages.error(request, 'Workshop ID and number of seats are required')
                return JsonResponse({
                    'status': 'error',
                    'message': 'Workshop ID and number of seats are required'
                }, status=400)

            # get workshop or return 404
            workshop = get_object_or_404(CandleWorkshop, id=workshop_id)

            try:
                # create booking using the class method
                booking = Booking.create_booking(
                    user=request.user,
                    workshop=workshop,
                    number_of_seats=number_of_seats
                )

                messages.success(
                    request, 
                    f'Successfully booked {number_of_seats} seat(s) for {workshop.title}'
                )

                return JsonResponse({
                    'status': 'success',
                    'message': 'Booking created successfully',
                    'booking': {
                        'id': booking.id,
                        'workshop_title': booking.workshop.title,
                        'number_of_seats': booking.number_of_seats,
                        'status': booking.status,
                        'booking_date': booking.booking_date.isoformat()
                    }
                })

            except ValidationError as e:
                error_message = str(e)
                messages.error(request, error_message)
                return JsonResponse({
                    'status': 'error',
                    'message': error_message
                }, status=400)

        except json.JSONDecodeError:
            messages.error(request, 'Invalid data received')
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            error_message = str(e)
            messages.error(request, f'An error occurred: {error_message}')
            return JsonResponse({
                'status': 'error',
                'message': error_message
            }, status=500)

class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "candle/dashboard/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_superuser:
            context['recent_bookings'] = Booking.objects.all()[:6]
            context['active_workshops'] = CandleWorkshop.objects.count()
            context['total_bookings'] = Booking.objects.count()
            context['total_blog_posts'] = Blogpost.objects.count()
            context['average_rating'] = Review.get_average_rating() 
        else:
            context['recent_bookings'] = Booking.objects.filter(user=user)[:6]
            context['total_bookings'] = Booking.objects.filter(user=user).count()
            context['total_blog_posts'] = Blogpost.objects.filter(author=user).count()
            context['average_rating'] = Review.get_average_rating(user=user) 

        return context

class BookingDeleteView(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Booking
    success_url = reverse_lazy('candle:dashboard')
    success_message = "Booking was deleted successfully."

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not (obj.user == self.request.user or self.request.user.is_superuser):
            raise PermissionDenied("You don't have permission to delete this booking.")
        return obj
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
    
class BookingUpdateView(LoginRequiredMixin, View):
    http_method_names = ['post']

    def get_object(self, pk):
        obj = get_object_or_404(Booking.objects.all(), pk=pk)
        if not (obj.user == self.request.user or self.request.user.is_superuser):
            raise PermissionDenied("You don't have permission to edit this booking.")
        return obj

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            booking = self.get_object(pk=data["bookingId"])
            
            if 'seats' in data:
                old_seats = booking.number_of_seats
                booking.number_of_seats = int(data['seats'])
                booking.status = data["status"]
                booking.save()
                
                messages.success(
                    request,
                    f'Booking updated successfully. Seats changed from {old_seats} to {booking.number_of_seats}.'
                )

            return JsonResponse({
                'status': 'success',
                'message': 'Booking updated successfully',
                'data': {
                    'id': booking.id,
                    'workshop_id': booking.workshop.id,
                    'seats': booking.number_of_seats,
                }
            })

        except json.JSONDecodeError:
            messages.error(request, 'Invalid JSON data provided.')
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid JSON data'
            }, status=400)

        except ValueError as e:
            messages.error(request, str(e))
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)

        except PermissionDenied as e:
            messages.error(request, str(e))
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=403)

        except Exception as e:
            messages.error(request, 'An unexpected error occurred while updating the booking.')
            return JsonResponse({
                'status': 'error',
                'message': 'An error occurred while updating the booking'
            }, status=500)

class DashboardBlogView(LoginRequiredMixin,TemplateView):
    template_name = "candle/dashboard/blogs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_superuser:
            context['blog_posts'] = Blogpost.objects.all()
        else:
            context['blog_posts'] = Blogpost.objects.filter(author=user)

        return context
    
class BlogDeleteView(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Blogpost
    success_url = reverse_lazy('candle:dashboard_blogs')
    success_message = "Blog was deleted successfully."

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not (obj.author == self.request.user or self.request.user.is_superuser):
            raise PermissionDenied("You don't have permission to delete this booking.")
        return obj
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)