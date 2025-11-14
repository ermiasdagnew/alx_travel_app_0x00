# ALX Travel App 0x00

This project demonstrates Django **database modeling**, **serialization**, and **data seeding** for the Listings module.

## Features
- **Listings** (title, description, price per night, location, availability)
- **Bookings** (ForeignKey → Listing)
- **Reviews** (ForeignKey → Listing)
- **Django REST Framework serializers** for Listing and Booking
- **Seeder command** to populate the database with sample data

## Setup and Commands

### 1. Run migrations
