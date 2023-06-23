from django import forms
from .models import Quote, Service, SubService, ContactUs, Booking


class QuoteForm(forms.ModelForm):
    name = forms.CharField(required=True, label='', max_length=500,  widget=forms.TextInput(attrs={
        'placeholder':'Full Name', 'id': 'name'
        }))
    phone = forms.CharField(required=True, label='', max_length=500,  widget=forms.TextInput(attrs={
        'placeholder':'Phone', 'id': 'phone'
        }))
    email = forms.EmailField(required=True, label='', max_length=500,  widget=forms.EmailInput(attrs={
        'placeholder':'Email', 'id': 'email'
        }))
    message = forms.CharField(required=True, label='', max_length=10000, widget=forms.Textarea(attrs={
        'placeholder':'Message', 'id': 'message'
        }))

    location = forms.CharField(required=True, label='', max_length=1000, widget=forms.TextInput(attrs={
        'placeholder':'Location', 'id': 'location'
        }))

    service = forms.ModelChoiceField(label='Service', queryset=Service.objects.all().order_by('-priority'),
     initial=Service.objects.order_by('-priority').first())

    sub_service = forms.ModelChoiceField(label='Service', 
        queryset=SubService.objects.all().order_by('-priority'), 
        initial=SubService.objects.filter(
            service=Service.objects.order_by('-priority').first().pk).order_by('-priority').first()
        )
    

    class Meta:
        model = Quote
        fields = ['name', 'phone', 'email', 'service', 'sub_service', 'location', 'message']


class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True, label='', max_length=500,  widget=forms.TextInput(attrs={
        'placeholder':'Full Name', 'id': 'name'
        }))
    phone = forms.CharField(required=True, label='', max_length=500,  widget=forms.TextInput(attrs={
        'placeholder':'Phone', 'id': 'phone'
        }))
    email = forms.EmailField(required=True, label='', max_length=500,  widget=forms.EmailInput(attrs={
        'placeholder':'Email', 'id': 'email'
        }))
    message = forms.CharField(required=True, label='', max_length=10000, widget=forms.Textarea(attrs={
        'placeholder':'Message', 'id': 'message'
        }))

    location = forms.CharField(required=True, label='', max_length=1000, widget=forms.TextInput(attrs={
        'placeholder':'Location', 'id': 'location'
        }))


    class Meta:
        model = ContactUs
        fields = ['name', 'phone', 'email', 'location', 'message']


class BookingForm(forms.ModelForm):
    name = forms.CharField(required=True, label='', max_length=500,  widget=forms.TextInput(attrs={
        'placeholder':'Full Name', 'id': 'name'
        }))
    phone = forms.CharField(required=True, label='', max_length=500,  widget=forms.TextInput(attrs={
        'placeholder':'Phone', 'id': 'phone'
        }))
    email = forms.EmailField(required=True, label='', max_length=500,  widget=forms.EmailInput(attrs={
        'placeholder':'Email', 'id': 'email'
        }))
    message = forms.CharField(required=True, label='', max_length=10000, widget=forms.Textarea(attrs={
        'placeholder':'Message', 'id': 'message'
        }))

    location = forms.CharField(required=True, label='', max_length=1000, widget=forms.TextInput(attrs={
        'placeholder':'Location', 'id': 'location'
        }))

    service = forms.ModelChoiceField(label='Service', queryset=Service.objects.all().order_by('-priority'),
     initial=Service.objects.order_by('-priority').first())

    sub_service = forms.ModelChoiceField(label='Service', 
        queryset=SubService.objects.all().order_by('-priority'), 
        initial=SubService.objects.filter(
            service=Service.objects.order_by('-priority').first().pk).order_by('-priority').first()
        )
    
    meeting_time = forms.DateTimeField(required=True, label='', widget=forms.DateTimeInput(attrs={
        'placeholder':'Meeting time', 'id': 'meeting_time', 'type': 'datetime-local'
        })) 

    class Meta:
        model = Booking
        fields = ['name', 'phone', 'email', 'service', 'sub_service', 'location', 'message', 'meeting_time']

