from django.contrib import admin
from .models import Listing, Booking, Review


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_night', 'available')
    search_fields = ('title', 'location')
    list_filter = ('available', 'location')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('listing', 'user_name', 'check_in', 'check_out', 'created_at')
    search_fields = ('user_name', 'listing__title')
    list_filter = ('check_in', 'check_out')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('listing', 'user_name', 'rating', 'created_at')
    search_fields = ('user_name', 'listing__title')
    list_filter = ('rating',)
