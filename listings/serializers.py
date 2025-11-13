from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    """Serializer for the Listing model."""

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'location', 'price_per_night', 'available', 'created_at']


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for the Booking model."""
    listing = ListingSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user_name', 'check_in', 'check_out', 'created_at']
