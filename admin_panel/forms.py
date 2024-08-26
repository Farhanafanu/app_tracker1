# forms.py
from django import forms
from .models import App

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ['image','name', 'link', 'category', 'sub_category', 'points']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'placeholder': 'App Name', 'class': 'form-control'}),
            'link': forms.URLInput(attrs={'placeholder': 'App Link', 'class': 'form-control'}),
            'category': forms.TextInput(attrs={'placeholder': 'App Category', 'class': 'form-control'}),
            'sub_category': forms.TextInput(attrs={'placeholder': 'Sub Category', 'class': 'form-control'}),
            'points': forms.NumberInput(attrs={'placeholder': 'Points', 'class': 'form-control'}),
        }
