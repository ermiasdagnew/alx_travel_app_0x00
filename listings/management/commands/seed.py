from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = "Seed the database with sample listing data"

    def handle(self, *args, **options):
        sample_data = [
            {
                "title": "Lake View Lodge",
                "description": "Beautiful lakeside cabin with amazing views.",
                "price_per_night": 120.00,
                "location": "Bahir Dar",
                "available": True,
            },
            {
                "title": "City Center Apartment",
                "description": "Modern apartment located in the heart of the city.",
                "price_per_night": 80.00,
                "location": "Addis Ababa",
                "available": True,
            },
            {
                "title": "Mountain Retreat",
                "description": "Quiet and peaceful home in the mountains.",
                "price_per_night": 150.00,
                "location": "Gondar",
                "available": False,
            },
        ]

        for item in sample_data:
            Listing.objects.get_or_create(**item)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
