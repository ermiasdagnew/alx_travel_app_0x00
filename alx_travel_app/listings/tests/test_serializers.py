from django.test import TestCase
from listings.models import Listing, Booking, Review
from listings.serializers import ListingSerializer, BookingSerializer, ReviewSerializer
from datetime import date, timedelta

class SerializerTestCase(TestCase):
    def setUp(self):
        self.listing = Listing.objects.create(
            name="Test Listing",
            description="A nice place",
            price_per_night=100,
            location="Addis Ababa"
        )
        self.booking = Booking.objects.create(
            listing=self.listing,
            guest_name="John Doe",
            start_date=date.today(),
            end_date=date.today() + timedelta(days=3)
        )
        self.review = Review.objects.create(
            listing=self.listing,
            reviewer_name="Alice",
            rating=5,
            comment="Great stay!"
        )

    def test_listing_serializer(self):
        serializer = ListingSerializer(self.listing)
        data = serializer.data
        self.assertEqual(data["name"], "Test Listing")
        self.assertIn("bookings", data)
        self.assertIn("reviews", data)

    def test_booking_serializer(self):
        serializer = BookingSerializer(self.booking)
        self.assertEqual(serializer.data["guest_name"], "John Doe")

    def test_review_serializer(self):
        serializer = ReviewSerializer(self.review)
        self.assertEqual(serializer.data["rating"], 5)
