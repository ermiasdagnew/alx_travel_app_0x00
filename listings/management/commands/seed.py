from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.utils import timezone
import random


class Command(BaseCommand):
    """Custom Django command to seed the database with sample data."""

    help = "Seed the database with sample listings, bookings, and reviews."

    def handle(self, *args, **kwargs):
        self.stdout.write("🌱 Starting database seeding...")

        # Clear existing data
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()

        # Create sample listings
        listings = []
        for i in range(5):
            listing = Listing.objects.create(
                title=f"Sample Listing {i + 1}",
                description="A beautiful place to stay during your trip.",
                location=random.choice(["Addis Ababa", "Bahir Dar", "Lalibela", "Hawassa", "Gondar"]),
                price_per_night=random.randint(50, 300),
                available=random.choice([True, False]),
            )
            listings.append(listing)

        # Create sample bookings
        for listing in listings:
            for j in range(random.randint(1, 3)):
                Booking.objects.create(
                    listing=listing,
                    user_name=f"User{j + 1}",
                    check_in=timezone.now().date(),
                    check_out=timezone.now().date() + timezone.timedelta(days=random.randint(1, 5)),
                )

        # Create sample reviews
        for listing in listings:
            for k in range(random.randint(1, 3)):
                Review.objects.create(
                    listing=listing,
                    user_name=f"Reviewer{k + 1}",
                    rating=random.randint(3, 5),
                    comment="Great experience! Highly recommended.",
                )

        self.stdout.write(self.style.SUCCESS("✅ Database seeding completed successfully!"))
