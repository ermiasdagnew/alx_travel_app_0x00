from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from listings import views

# DRF router for Listing and Booking viewsets
router = routers.DefaultRouter()
router.register(r'listings', views.ListingViewSet, basename='listing')
router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API routes for listings and bookings
]
