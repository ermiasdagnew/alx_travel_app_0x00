from django.test import TestCase
from django.core.management import call_command
from listings.models import Listing, Booking, Review

class SeedTestCase(TestCase):
    def test_seed_command(self):
        # Run the seed command
        call_command("seed")
        
        # Check that listings, bookings, and reviews were created
        self.assertTrue(Listing.objects.count() > 0)
        self.assertTrue(Booking.objects.count() > 0)
        self.assertTrue(Review.objects.count() > 0)
