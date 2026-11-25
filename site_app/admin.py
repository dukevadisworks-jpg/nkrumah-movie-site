from django.contrib import admin
from .models import Movie, GalleryImage, Service, Product, Booking, ContactMessage, SiteSettings

for model in (Movie, GalleryImage, Service, Product, Booking, ContactMessage), SiteSettings:
    admin.site.register(model)