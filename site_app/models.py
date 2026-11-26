from cloudinary.models import CloudinaryField
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=250, blank=True)
    synopsis = models.TextField()
    poster = CloudinaryField('poster', blank=True, null=True)
    hero_image = CloudinaryField('hero image', blank=True, null=True)
    trailer_url = models.URLField(blank=True, help_text='YouTube or Cloudinary video link')
    release_info = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    caption = models.CharField(max_length=200, blank=True)
    image = CloudinaryField('image')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.caption or f'Image {self.pk}'


class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = CloudinaryField('photo', blank=True, null=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    event_type = models.CharField(max_length=120, help_text='Screening, talk, interview...')
    preferred_date = models.DateField()
    message = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.event_type}'


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.email})'


class SiteSettings(models.Model):
    logo = CloudinaryField('logo', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Site settings'

    def __str__(self):
        return 'Site settings'