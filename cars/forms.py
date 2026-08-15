from django import forms
from .models import TestDrive

TIME_SLOTS = [
    ('', 'Select a time'),
    ('10:00 AM', '10:00 AM'),
    ('11:00 AM', '11:00 AM'),
    ('1:00 PM', '1:00 PM'),
    ('3:00 PM', '3:00 PM'),
    ('4:30 PM', '4:30 PM'),
]

class TestDriveForm(forms.ModelForm):
    class Meta:
        model = TestDrive
        fields = ['name', 'email', 'phone', 'car', 'date', 'time_slot']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'car': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time_slot': forms.Select(attrs={'class': 'form-control'}, choices=TIME_SLOTS),
        }