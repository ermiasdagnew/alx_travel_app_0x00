from django.db import models


class Listing(models.Model):
    """Represents a travel property or listing available for booking."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """Represents a customer booking for a listing."""
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    user_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.listing.title}"


class Review(models.Model):
    """Represents a user review for a listing."""
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user_name} ({self.rating}/5)"
