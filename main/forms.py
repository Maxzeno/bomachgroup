from django import forms
from .models import Quote, Service, SubService


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
        'placeholder':'Massage', 'id': 'message'
        }))

    location = forms.CharField(required=True, label='', max_length=1000, widget=forms.TextInput(attrs={
        'placeholder':'Location', 'id': 'location'
        }))

    service = forms.ModelChoiceField(label='Service', queryset=Service.objects.all(), initial=Service.objects.first())

    sub_service = forms.ModelChoiceField(label='Service', 
        queryset=SubService.objects.all(), 
        initial=SubService.objects.filter(service=Service.objects.first().pk).first()
        )

    class Meta:
        model = Quote
        fields = ['name', 'phone', 'email', 'service', 'sub_service', 'location', 'message']

