from django import forms
from .models import Booking, ContactMessage


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'event_type', 'preferred_date', 'message']
        widgets = {'preferred_date': forms.DateInput(attrs={'type': 'date'})}


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']