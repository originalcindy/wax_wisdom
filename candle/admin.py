from django.contrib import admin
from .models import Blogpost, CandleWorkshop, Review, Booking,Config


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    def has_add_permission(self, request):
        # Only allow one configuration object
        return not Config.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the configuration
        return False
    
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
