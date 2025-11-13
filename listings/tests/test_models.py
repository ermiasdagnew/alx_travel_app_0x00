from django.test import TestCase
from listings.models import Listing, Booking, Review
from datetime import date, timedelta

class ListingModelTest(TestCase):
    def setUp(self):
        self.listing = Listing.objects.create(
            name="Test Listing",
            description="A nice place",
            price_per_night=100,
            location="Addis Ababa"
        )

    def test_listing_str(self):
        self.assertEqual(str(self.listing), "Test Listing")


class BookingModelTest(TestCase):
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

    def test_booking_str(self):
        self.assertEqual(str(self.booking), f"John Doe - {self.booking.listing.name}")


class ReviewModelTest(TestCase):
    def setUp(self):
        self.listing = Listing.objects.create(
            name="Test Listing",
            description="A nice place",
            price_per_night=100,
            location="Addis Ababa"
        )
        self.review = Review.objects.create(
            listing=self.listing,
            reviewer_name="Alice",
            rating=5,
            comment="Great stay!"
        )

    def test_review_str(self):
        self.assertEqual(str(self.review), f"Alice - {self.review.listing.name}")
