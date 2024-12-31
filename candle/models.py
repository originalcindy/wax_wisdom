from django.db import models
from django.db.models import Avg
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone
import math


User = get_user_model() 


class Config(models.Model):
    site_name = models.CharField(max_length=255)
    site_title = models.CharField(max_length=255)
    site_description = models.TextField()
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    pinterest_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Configuration'
        verbose_name_plural = 'Site Configuration'

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        if Config.objects.exists() and not self.pk:
            # if a Config object exists
            # update the existing one instead
            raise ValidationError('Only one configuration allowed')
        return super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        return cls.objects.first()
    
    def as_dict(self):
        return {
            'site_name': self.site_name or '',
            'site_title': self.site_title or '',
            'site_description': self.site_description or '',
            'facebook_url': self.facebook_url or '',
            'instagram_url': self.instagram_url or '',
            "pinterest_url": self.pinterest_url or ""
        }
    
class Blogpost(models.Model):
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='blogposts', 
        related_query_name='blogpost'
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(
        upload_to='blog_thumbnails/',
        null=True,
        blank=True,
        help_text='Featured image for the blog post'
    )

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ("-published_date",)

    def get_read_time(self):
        """
        calculate the read time of the blog post
        """
        word_count = len(self.content.split())
        reading_speed = 200 
        read_time = word_count / reading_speed
        return math.ceil(read_time)
    
    def get_read_time_display(self):
        """
        returns a formatted string of the read time
        """
        minutes = self.get_read_time()
        if minutes == 1:
            return "1 minute read"
        return f"{minutes} minutes read"


class CandleWorkshop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.FloatField(
        help_text='Duration of the workshop in hours (e.g., 1.5 for 1.5 hours)'
    )
    thumbnail = models.ImageField(
        upload_to='workshop_thumbnails/',
        null=True,
        blank=True,
        help_text='Featured image for the workshop'
    )
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()

    def __str__(self):
        return self.title

    def get_remaining_seats(self):
        """
        calculate the number of remaining seats for the workshop
        """
        total_booked_seats = Booking.objects.filter(
            workshop=self,
            status__in=['confirmed', 'pending']
        ).aggregate(
            total=models.Sum('number_of_seats')
        )['total'] or 0
        
        return self.capacity - total_booked_seats
    
    @property
    def formatted_duration(self):
        return int(self.duration) if self.duration.is_integer() else self.duration
    
    def get_reviews(self):
        """get all reviews for this workshop"""
        return self.reviews.all()

    def get_average_rating(self):
        """get average rating for this workshop"""
        avg_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return avg_rating if avg_rating is not None else 5.0
    
    def has_user_booked(self, user):
        """check if user has already booked this workshop"""
        return self.bookings.filter(
            user=user,
            status__in=['confirmed', 'pending']
        ).exists()
    
    class Meta:
        ordering = ("-date",)
    


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews', related_query_name='review'
    )
    workshop = models.ForeignKey(
        CandleWorkshop, on_delete=models.CASCADE, related_name='reviews', related_query_name='review'
    )
    rating = models.IntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.workshop.title}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', related_query_name='booking')
    workshop = models.ForeignKey(CandleWorkshop, on_delete=models.CASCADE, related_name='bookings', related_query_name='booking')
    booking_date = models.DateTimeField(auto_now_add=True)
    number_of_seats = models.IntegerField()
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='pending'
    )

    def __str__(self):
        return f"Booking by {self.user.username} for {self.workshop.title}"

    def clean(self):
        # check if workshop date hasn't passed
        if self.workshop.date < timezone.now().date():
            raise ValidationError("Cannot book a workshop that has already passed")
        
        # calculate available seats
        total_booked_seats = Booking.objects.filter(
            workshop=self.workshop,
            status__in=['confirmed', 'pending']
        ).exclude(pk=self.pk).aggregate(
            total=models.Sum('number_of_seats')
        )['total'] or 0
        
        available_seats = self.workshop.capacity - total_booked_seats
        
        # check if enough seats are available
        if self.number_of_seats > available_seats:
            raise ValidationError(f"Only {available_seats} seats available")
        
        # validate number of seats is positive
        if self.number_of_seats <= 0:
            raise ValidationError("Number of seats must be positive")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @classmethod
    def create_booking(cls, user, workshop, number_of_seats):
        """
        create a new booking for a user
        """
        booking = cls(
            user=user,
            workshop=workshop,
            number_of_seats=number_of_seats
        )
        booking.save()
        return booking

    def update_booking(self, number_of_seats=None, status=None):
        """
        update an existing booking
        """
        if number_of_seats is not None:
            self.number_of_seats = number_of_seats
        if status is not None:
            self.status = status
        self.save()

    def cancel_booking(self):
        """
        cancel a booking
        """
        self.status = 'cancelled'
        self.save()

    def __str__(self):
        return f"Booking by {self.user.username} for {self.workshop.title}"

    class Meta:
        ordering = ['-booking_date']