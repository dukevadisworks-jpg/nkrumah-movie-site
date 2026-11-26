from django.contrib import admin

from .models import (
    Booking,
    ContactMessage,
    GalleryImage,
    Movie,
    Product,
    Service,
    SiteSettings,
)

admin.site.register(Movie)
admin.site.register(GalleryImage)
admin.site.register(Service)
admin.site.register(Product)
admin.site.register(Booking)
admin.site.register(ContactMessage)
admin.site.register(SiteSettings)