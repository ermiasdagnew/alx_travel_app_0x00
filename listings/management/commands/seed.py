from django.core.management.base import BaseCommand
from django_seed import Seed
from listings.models import Listing, Booking
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings and bookings"

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        # Make sure you have users in the DB
        users = User.objects.all()
        if not users:
            self.stdout.write(self.style.ERROR("No users found. Please create some users first."))
            return

        # Seed Listings
        seeder.add_entity(Listing, 10, {
            'owner': lambda x: random.choice(users),
        })

        # Seed Bookings
        seeder.add_entity(Booking, 20, {
            'user': lambda x: random.choice(users),
            'listing': lambda x: Listing.objects.order_by('?').first()
        })

        inserted_pks = seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"Seeded database: {inserted_pks}"))
