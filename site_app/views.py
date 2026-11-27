from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import BookingForm, ContactForm
from .models import Movie, GalleryImage, Service, Product


def home(request):
    return render(request, 'home.html', {
        'movie': Movie.objects.first(),
        'gallery': GalleryImage.objects.all()[:6],
    })


def about(request):
    return render(request, 'about.html', {'movie': Movie.objects.first()})


def services(request):
    return render(request, 'services.html', {'services': Service.objects.all()})


def products(request):
    return render(request, 'products.html', {'products': Product.objects.all()})


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Thank you! Your message has been sent.')
        return redirect('contact')
    return render(request, 'contact.html', {'form': form})


def booking(request):
    form = BookingForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Your booking request has been received. We will be in touch.')
        return redirect('booking')
    return render(request, 'booking.html', {'form': form})


def health(request):
    return JsonResponse({'status': 'ok'})