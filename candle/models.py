from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

class Blogpost(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blogposts', related_query_name='blogpost'
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title


class CandleWorkshop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews', related_query_name='review'
    )
    workshop = models.ForeignKey(
        CandleWorkshop, on_delete=models.CASCADE, related_name='reviews', related_query_name='review'
    )
    rating = models.IntegerField()
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
