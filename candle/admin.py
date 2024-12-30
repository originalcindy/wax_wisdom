from django.contrib import admin
from .models import Blogpost, CandleWorkshop, Review, Booking

@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author__username', 'content')


@admin.register(CandleWorkshop)
class CandleWorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'price', 'capacity')
    search_fields = ('title', 'description')
    list_filter = ('date',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'workshop', 'rating', 'created_at')
    search_fields = ('user__username', 'workshop__title', 'comment')
    list_filter = ('rating', 'created_at')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'workshop', 'booking_date', 'number_of_seats', 'status')
    search_fields = ('user__username', 'workshop__title', 'status')
    list_filter = ('status', 'booking_date')
