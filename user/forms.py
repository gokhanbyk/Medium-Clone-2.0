from django import forms
from tinymce.widgets import TinyMCE
from .models import *
from django.core import validators


class ProfileModelForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'avatar',
            'instagram',
            'info',
        ]